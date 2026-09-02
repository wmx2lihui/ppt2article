# Reference Manager Design v2.6

## Purpose

Manage literature retrieval and citation support.

## Functions

1. Extract claims requiring citations.
2. Match claims with relevant papers.
3. Maintain BibTeX records.
4. Verify citation consistency.

Pipeline:

```
Claim
 |
Literature Search
 |
Evidence Matching
 |
BibTeX Entry
 |
Manuscript Citation
```

The system should avoid adding citations that do not actually support the statement.
