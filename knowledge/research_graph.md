# Research Knowledge Graph

## Purpose

Build a persistent knowledge representation layer for scientific paper generation.

The graph connects:

- scientific problems
- methods
- theories
- experiments
- datasets
- researchers
- journals
- references

## Core Nodes

```yaml
problem:
method:
algorithm:
theory:
experiment:
paper:
author:
journal:
```

## Core Relations

- method solves problem
- paper proposes method
- experiment validates method
- journal prefers contribution type
- reference supports claim

## Usage

The graph provides context for future manuscript generation and avoids isolated paper writing.
