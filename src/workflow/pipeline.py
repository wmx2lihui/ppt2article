"""Minimal end-to-end pipeline for ppt2article MVP.

Pipeline:
input -> memory -> outline -> latex
"""

from pathlib import Path

from core.memory_store import ResearchMemory
from generator.latex_builder import LatexBuilder
from parser.ppt_parser import parse_ppt


def run_pipeline(input_file: str, output_dir: str = "paper_project"):
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)

    memory = parse_ppt(input_file)
    ResearchMemory(output / "research_memory.json").save(memory)

    LatexBuilder(output / "main.tex").build(memory)

    return output
