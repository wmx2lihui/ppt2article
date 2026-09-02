# ppt2article Master Workflow

## Goal

Convert scientific PPT materials into a complete submission-ready LaTeX paper package.

## Pipeline

### Stage 1: Scientific Mining

Input:
- PPT/PDF slides
- Notes
- Existing figures

Output:
- Research knowledge graph
- Problem definition
- Method summary
- Candidate contributions

### Stage 2: Research Architecture

Tasks:
- Identify novelty
- Select target journal
- Design manuscript structure
- Determine missing experiments

### Stage 3: Manuscript Construction

Generate:
- abstract.tex
- introduction.tex
- methodology.tex
- experiments.tex
- results.tex
- conclusion.tex

### Stage 4: Evidence System

Generate:
- reference.bib
- citation mapping
- related work analysis

### Stage 5: Review Simulation

Agents:

1. Domain expert reviewer
2. Numerical/method reviewer
3. Journal editor

### Stage 6: Submission Package

Output:

```
submission_package/
├── main.tex
├── reference.bib
├── sections/
├── figures/
├── tables/
├── cover_letter/
├── highlights/
└── response_to_reviewers/
```
