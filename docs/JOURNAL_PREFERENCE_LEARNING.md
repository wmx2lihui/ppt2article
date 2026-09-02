# Journal Preference Learning Protocol

## Motivation

Different journals have different expectations. A manuscript accepted by one journal may not fit another because the scientific story, contribution emphasis, and presentation style differ.

ppt2article should learn these differences before generating the manuscript.

## Learning Sources

The agent may analyze:

- recent highly cited papers
- recently published papers
- journal author guidelines
- review articles

## Extracted Features

### Scientific Scope

- research topics
- accepted methodologies
- application domains

### Contribution Pattern

Examples:

- new theory
- new computational framework
- new experimental evidence
- new understanding of mechanism

### Writing Pattern

Analyze:

- introduction organization
- paragraph transition logic
- method explanation depth
- result discussion style

### Visualization Pattern

Analyze:

- number of figures
- figure arrangement
- preferred schematic style
- quantitative comparison style

## Output

journal_profile.yaml

Example:

```yaml
journal:
  name:

story:
  preferred_contribution:
  expected_depth:

writing:
  introduction_style:
  discussion_style:

review:
  common_rejection_reason:
```

## Usage

The manuscript generator receives both:

1. research_memory.yaml
2. journal_profile.yaml

and produces a journal-specific manuscript strategy.
