# Input Manager

## Purpose
Manage all research inputs before paper generation.

Supported inputs:
- PPT/PPTX
- PDF papers
- Supplementary materials
- Dataset descriptions
- Code repositories
- Target journal information

## Input normalization
All files are converted into a unified research package:

```
project_input/
├── slides/
├── references/
├── figures/
├── data/
└── metadata.yaml
```

The manager records provenance and ensures every generated claim can be traced back to an input source.
