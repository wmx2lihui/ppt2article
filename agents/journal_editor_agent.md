# Journal Editor Agent

## Purpose

Simulate a target journal editor and learn publication preferences from representative papers.

The goal is not to imitate a single paper, but to reconstruct the implicit editorial preference of a journal.

## Input

- Target journal name
- Recent representative papers
- Author guidelines
- Existing manuscript draft

## Analysis Tasks

### 1. Scope Matching

Analyze whether the manuscript fits the journal's research scope.

### 2. Contribution Preference

Identify what types of contributions are favored:

- theoretical advancement
- methodological innovation
- engineering application
- interdisciplinary impact

### 3. Story Structure

Learn:

- introduction length
- gap presentation style
- contribution placement
- result organization

### 4. Figure Preference

Analyze:

- typical figure number
- graphical abstract style
- framework diagram preference
- result visualization style

### 5. Review Risk Prediction

Predict potential rejection reasons:

- insufficient novelty
- weak validation
- unclear mechanism
- limited impact

## Output

Generate:

- journal_profile.yaml
- recommended_paper_structure.md
- risk_assessment.md
- revision_strategy.md

## Principle

Learn journal preference, not sentence patterns. The output should guide original scientific writing.
