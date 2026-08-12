from pathlib import Path
import json, subprocess, tempfile, yaml, re
ROOT=Path(__file__).resolve().parents[1]
BUILDER=ROOT/'PASS/tools/build_release.py'

def run(*args): return subprocess.run(['python',str(BUILDER),*map(str,args)],text=True,capture_output=True)

def test_named_releases_build_and_include_metaskills():
    for recipe in (ROOT/'workspace/release-recipes').glob('*.yaml'):
        with tempfile.TemporaryDirectory() as td:
            out=Path(td)/'release'; r=run('build',recipe,out); assert r.returncode==0,r.stderr
            assert (out/'modules/metaskills/MODULE.yaml').is_file()
            assert run('check',out).returncode==0

def test_cpp_excludes_art():
    with tempfile.TemporaryDirectory() as td:
        out=Path(td)/'release'; r=run('build',ROOT/'workspace/release-recipes/CPP_Development.yaml',out); assert r.returncode==0,r.stderr
        mf=json.loads((out/'RELEASE_MANIFEST.json').read_text())
        assert 'software-engineering/core' in mf['modules']
        assert all(not x.startswith('art/') for x in mf['modules'])

def test_missing_module_fails_closed():
    with tempfile.TemporaryDirectory() as td:
        rp=Path(td)/'bad.yaml'; rp.write_text('name: bad\nmodules: [does/not/exist]\n')
        out=Path(td)/'out'; r=run('build',rp,out); assert r.returncode!=0

def test_no_agent_or_git_plumbing_in_workspace():
    assert not (ROOT/'.agents').exists(); assert not (ROOT/'.claude').exists()
