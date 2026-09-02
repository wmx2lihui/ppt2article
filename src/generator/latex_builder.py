"""Minimal LaTeX project generator for ppt2article MVP."""

from pathlib import Path


MAIN_TEX = r"""\documentclass{article}
\begin{document}
\title{Generated Research Manuscript}
\maketitle

\section{Introduction}
Generated from research memory.

\section{Method}

\section{Results}

\end{document}
"""


def generate_latex(output_dir: str):
    folder = Path(output_dir)
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "main.tex").write_text(MAIN_TEX, encoding="utf-8")
