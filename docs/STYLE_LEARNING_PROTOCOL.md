# Style Learning Protocol

## Overview

ppt2article supports learning the writing style of a given reference paper.

This module is designed for academic style transfer, not content imitation.

The system learns the author's scientific communication strategy and applies it to a new research topic.

---

# Workflow

```
Reference Paper
      |
      v
Style Extraction
      |
      v
Style Profile
      |
      v
Manuscript Generation
      |
      v
Style Consistency Review
```

---

# Reference Paper Analysis

The system analyzes:

## 1. Introduction Style

Extract:

- how background is introduced
- how research gap is constructed
- how contributions are announced

## 2. Method Section Style

Extract:

- equation explanation order
- assumption presentation
- algorithm description depth

## 3. Results Style

Extract:

- whether results start from observation or mechanism
- how comparisons are organized
- how limitations are discussed

## 4. Discussion Style

Extract:

- scientific interpretation
- engineering implication
- future perspective

---

# Style Transfer Levels

## Level 1: Structural Style

Learn:

- section arrangement
- subsection hierarchy
- storytelling order

## Level 2: Paragraph Style

Learn:

- paragraph length
- transition patterns
- information density

## Level 3: Expression Style

Learn:

- terminology preference
- academic tone
- sentence patterns

---

# Safety Constraints

The system must not:

- copy sentences;
- reproduce unique phrases;
- imitate unpublished content;
- transfer scientific claims.

The system only transfers general academic writing characteristics.

---

# Integration

The Style Transfer Agent communicates with:

- PPT Mining Agent
- Literature Agent
- LaTeX Agent
- Reviewer Agent

The final manuscript should preserve:

scientific originality + target journal style.
