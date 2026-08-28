# Batches

Each bounded empirical batch has one explicit YAML artifact named after its
`batch_id`. `state.yaml` points to the current batch file, and repository tests
require that pointer to resolve and match the declared ID.
