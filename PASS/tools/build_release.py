#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re, shutil, sys, zipfile
from pathlib import Path
import yaml
FM_RE=re.compile(r'\A---\r?\n(?P<front>.*?)\r?\n---\r?\n(?P<body>.*)\Z',re.S)
FORBIDDEN={'.git','.agents','.claude','__pycache__','.pytest_cache','workspace','sources','ledger','ledgers','worklogs','trash','tmp','build','dist'}

def read_yaml(p):
    d=yaml.safe_load(p.read_text(encoding='utf-8'))
    if not isinstance(d,dict): raise ValueError(f'{p}: expected mapping')
    return d

def discover(lib):
    out={}
    for p in lib.rglob('MODULE.yaml'):
        d=read_yaml(p); name=d.get('name')
        if not isinstance(name,str) or not name: raise ValueError(f'{p}: module name missing')
        if name in out: raise ValueError(f'duplicate module name: {name}')
        expected=p.parent.relative_to(lib).as_posix()
        if name!=expected: raise ValueError(f'{p}: module name/path mismatch: {name} != {expected}')
        out[name]=(p.parent,d)
    return out

def object_index(lib, modules):
    byid={}; owner={}
    module_dirs=sorted(((path,name) for name,(path,_d) in modules.items()),key=lambda x:len(x[0].parts),reverse=True)
    for p in lib.rglob('*.md'):
        raw=p.read_text(encoding='utf-8'); m=FM_RE.match(raw)
        if not m: continue
        d=yaml.safe_load(m.group('front'))
        if not isinstance(d,dict) or not d.get('object_id'): continue
        oid=d['object_id']
        if oid in byid: raise ValueError(f'duplicate object_id: {oid}')
        byid[oid]=(p,d)
        for md,name in module_dirs:
            try: p.relative_to(md); owner[oid]=name; break
            except ValueError: pass
    return byid,owner

def resolve(entry,modules,byid,owner):
    selected=set(); visiting=set()
    def addmod(name):
        if name in selected: return
        if name in visiting: raise ValueError(f'module dependency cycle at {name}')
        if name not in modules: raise ValueError(f'missing module: {name}')
        visiting.add(name)
        for r in modules[name][1].get('requires') or []: addmod(r)
        visiting.remove(name); selected.add(name)
    addmod('metaskills')
    for n in entry: addmod(n)
    changed=True
    while changed:
        changed=False
        included_ids={oid for oid,m in owner.items() if m in selected}
        for oid in list(included_ids):
            d=byid[oid][1]
            fid=d.get('foundation_object_id')
            if fid and fid!='none':
                if fid not in byid: raise ValueError(f'{oid}: missing foundation object {fid}')
                mod=owner.get(fid)
                if not mod: raise ValueError(f'{oid}: foundation object has no module: {fid}')
                before=len(selected); addmod(mod); changed |= len(selected)!=before
        # prerequisite_for points from prerequisite source -> dependent target.
        for src,(p,d) in byid.items():
            for link in d.get('cross_links') or []:
                if isinstance(link,dict) and link.get('rel')=='prerequisite_for':
                    tgt=link.get('target_object_id')
                    if tgt in included_ids:
                        if src not in byid: raise ValueError(f'{tgt}: missing prerequisite {src}')
                        mod=owner.get(src)
                        if not mod: raise ValueError(f'{src}: prerequisite has no module')
                        before=len(selected); addmod(mod); changed |= len(selected)!=before
    return selected

def scan_tree(path):
    problems=[]
    for p in path.rglob('*'):
        rel=p.relative_to(path)
        if any(part in FORBIDDEN for part in rel.parts): problems.append(f'forbidden path: {rel}')
        if p.is_symlink(): problems.append(f'symlink: {rel}')
        if p.is_file() and p.suffix.lower() in {'.md','.yaml','.yml','.json','.py','.txt'}:
            text=p.read_text(encoding='utf-8',errors='ignore')
            if '/mnt/data/' in text or re.search(r'(?m)(?:^|[\s`"\'])\.\./',text): problems.append(f'external path reference: {rel}')
            if 'SkillForge_Base' in text: problems.append(f'factory dependency reference: {rel}')
    return sorted(set(problems))

def build(recipe, outdir, zip_out=None, library=None):
    lib=(library or (Path.cwd()/'library')).resolve()
    if not lib.is_dir(): raise ValueError(f'library root not found: {lib}; pass --library')
    modules=discover(lib); byid,owner=object_index(lib,modules)
    spec=read_yaml(recipe); entries=spec.get('modules') or []
    if not entries: raise ValueError('release recipe has no modules')
    selected=resolve(entries,modules,byid,owner)
    if outdir.exists(): shutil.rmtree(outdir)
    (outdir/'modules').mkdir(parents=True)
    selected_roots={modules[n][0].resolve() for n in selected}
    def ignore_nested_modules(current, names):
        cur=Path(current).resolve()
        ignored=[]
        for item in names:
            child=(cur/item).resolve()
            if child != cur and child in selected_roots:
                ignored.append(item)
        return ignored
    # Copy broader modules first while pruning nested selected modules; then overlay the nested modules.
    for name in sorted(selected, key=lambda n: len(modules[n][0].parts)):
        src=modules[name][0]; dst=outdir/'modules'/name
        shutil.copytree(src,dst,dirs_exist_ok=True,ignore=ignore_nested_modules)
    manifest={'name':spec.get('name',recipe.stem),'modules':sorted(selected)}
    (outdir/'RELEASE_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    (outdir/'SKILL.md').write_text('# '+manifest['name']+'\n\nThis is a self-contained SkillForge release. Load `modules/metaskills` as the universal process baseline, then use the bundled domain modules relevant to the task. Hard prerequisites have been materialized locally. Source citations are provenance, not runtime dependencies.\n\n## Bundled modules\n\n'+''.join(f'- `{m}`\n' for m in manifest['modules']),encoding='utf-8')
    problems=scan_tree(outdir)
    if problems: raise ValueError('release portability check failed:\n'+'\n'.join(problems))
    if zip_out:
        zip_out.parent.mkdir(parents=True,exist_ok=True)
        with zipfile.ZipFile(zip_out,'w',zipfile.ZIP_DEFLATED) as z:
            for p in sorted(outdir.rglob('*')):
                if p.is_file(): z.write(p,p.relative_to(outdir.parent))
    return manifest

def check(path):
    probs=scan_tree(path)
    mf=path/'RELEASE_MANIFEST.json'
    if not mf.is_file(): probs.append('missing RELEASE_MANIFEST.json')
    if not (path/'SKILL.md').is_file(): probs.append('missing SKILL.md')
    if not (path/'modules/metaskills/MODULE.yaml').is_file(): probs.append('missing mandatory metaskills')
    if probs: raise ValueError('\n'.join(probs))

def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='cmd',required=True)
    b=sub.add_parser('build'); b.add_argument('recipe',type=Path); b.add_argument('outdir',type=Path); b.add_argument('--library',type=Path); b.add_argument('--zip',dest='zip_out',type=Path)
    c=sub.add_parser('check'); c.add_argument('path',type=Path)
    a=ap.parse_args()
    try:
        if a.cmd=='build':
            m=build(a.recipe.resolve(),a.outdir.resolve(),a.zip_out.resolve() if a.zip_out else None,a.library.resolve() if a.library else None); print(json.dumps(m,indent=2))
        else: check(a.path.resolve()); print('PASS: portable release')
    except Exception as e:
        print(f'FAIL: {e}',file=sys.stderr); return 1
    return 0
if __name__=='__main__': raise SystemExit(main())
