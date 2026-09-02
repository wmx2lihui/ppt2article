# Agent Architecture v2.6

## Goal

Provide modular scientific agents for the paper generation pipeline.

## Core Agents

- Scientific Writer Agent
  - Converts research memory into academic manuscript sections.

- Literature Agent
  - Retrieves and organizes supporting references.

- Reviewer Agent
  - Simulates peer review and identifies weaknesses.

- Style Agent
  - Adapts writing style according to target journals and reference papers.

## Shared Context

All agents communicate through Research Memory rather than independent prompts.

Input:

```yaml
research_memory:
target_journal:
style_profile:
feedback_history:
```

Output:

```yaml
analysis:
artifacts:
confidence:
recommendations:
```
