# LATEX_ENGINE

## Goal

Generate a complete journal-ready LaTeX project instead of plain manuscript text.

## Output Structure

```
submission_package/
├── main.tex
├── reference.bib
├── sections/
├── figures/
├── tables/
├── appendix/
└── cover_letter/
```

## Rules

1. Every section is stored as an independent tex file.
2. Figures are referenced using labels and captions.
3. Tables are generated as reusable LaTeX components.
4. Citations must map to BibTeX entries.
5. Compilation must succeed without manual repair.

## Main Template

```latex
\\documentclass{journal_template}

\\begin{document}
\\input{sections/abstract}
\\input{sections/introduction}
\\input{sections/methodology}
\\input{sections/results}
\\bibliography{reference}
\\end{document}
```

The LaTeX agent is responsible for formatting, consistency checking, and journal adaptation.
