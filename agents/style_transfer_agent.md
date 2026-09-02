# Style Transfer Agent

## Purpose

The Style Transfer Agent enables ppt2article to learn the writing characteristics of a target scientific paper and reproduce its academic presentation style while generating a new manuscript.

The goal is not copying content, but learning:

- logical organization
- argument progression
- paragraph rhythm
- terminology preference
- mathematical explanation style
- figure discussion style
- result interpretation style

---

## Input

Required:

- target paper PDF
- target journal information
- research_memory.yaml of the new work

Optional:

- several papers from the same research group
- author's previous publications

---

## Style Analysis Output

Generate `style_profile.yaml`:

```yaml
journal_style:
  structure:
  section_order:

writing_style:
  sentence_length:
  paragraph_pattern:
  transition_style:

technical_style:
  equation_explanation:
  figure_description:
  result_discussion:

preferred_expression:
  use:
  avoid:
```

---

## Analysis Dimensions

### 1. Paper Architecture

Analyze:

- introduction construction
- motivation building
- gap presentation
- contribution statement
- conclusion strategy

### 2. Paragraph Logic

Extract patterns:

Problem → limitation → solution → evidence

or

Observation → mechanism → explanation → implication

### 3. Academic Language

Learn:

- preferred verbs
- technical phrases
- degree of assertiveness
- passive/active voice preference

### 4. Figure Narration

Analyze how the paper:

- introduces figures
- explains trends
- connects figures with conclusions

---

## Generation Rules

The generated manuscript should:

1. follow the learned writing pattern;
2. maintain original scientific content;
3. avoid sentence-level imitation;
4. avoid plagiarism;
5. preserve citation integrity.

---

## Workflow

Target Paper PDF

↓

Style Analysis

↓

style_profile.yaml

↓

LaTeX Generation Agent

↓

Manuscript Revision

↓

Reviewer Simulation

