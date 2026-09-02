# DATA_SCHEMA

## Purpose

Define the intermediate data representation between agents in ppt2article.

The system should not directly transform PPT into text. All agents communicate through structured research memory.

## Research Memory

```yaml
project:
  title:
  field:
  target_journal:

problem:
  scientific_gap:
  engineering_need:

method:
  theory:
  algorithm:
  implementation:

contributions:
  - statement:
    evidence:
    importance:

experiments:
  datasets:
  parameters:
  metrics:

figures:
  - name:
    purpose:
    section:

references:
  - topic:
    bibkey:
```

## Principle

Every generated paragraph, figure, table, and citation must be traceable to this research memory.
