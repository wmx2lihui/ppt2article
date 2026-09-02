# Paper Memory Schema

The central data structure shared among agents.

```yaml
paper:
  title:
  field:
  target_journal:

problem:
  background:
  scientific_gap:
  limitations:

method:
  theory:
  algorithm:
  implementation:

contributions:
  - description:
    novelty_level:

experiments:
  benchmark:
  metrics:
  findings:

figures:
  - name:
    purpose:
    section:

references:
  - key:
    role:
```

All agents should read and update this memory instead of creating isolated summaries.
