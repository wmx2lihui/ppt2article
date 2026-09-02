# Parser Layer Design

## Goal

Convert PPT/PDF scientific materials into structured research information.

## Supported Inputs

- PPTX slides
- PDF papers
- Figures
- Tables
- Supplementary materials

## Pipeline

```text
Input Files
  -> Text Extraction
  -> Figure Extraction
  -> Equation Recognition
  -> Semantic Understanding
  -> Research Memory
```

## Output

research_memory.json
