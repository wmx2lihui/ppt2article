# ppt2article Source Architecture

Planned implementation structure:

```
src/
├── core/
│   ├── memory/
│   ├── workflow/
│   └── agents/
├── parser/
│   ├── ppt_parser.py
│   ├── pdf_parser.py
│   └── figure_parser.py
├── generator/
│   ├── latex_generator.py
│   └── bib_generator.py
├── validator/
│   ├── latex_checker.py
│   └── citation_checker.py
└── cli/
    └── main.py
```

The first implementation prioritizes modularity and replaceable AI backends.
