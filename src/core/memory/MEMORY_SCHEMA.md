# Research Memory Schema

The central data object shared by all agents.

```yaml
project:
problem:
  background:
  gap:
  objective:

method:
  idea:
  algorithm:
  implementation:

experiments:
  datasets:
  baselines:
  findings:

figures:
references:
review_feedback:
```

All generation modules should read and update this memory instead of relying on isolated context.
