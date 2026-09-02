"""MVP PPT parser placeholder for ppt2article.

The first implementation focuses on extracting structured research
information from slides. Future versions will integrate multimodal models.
"""

from pathlib import Path


def parse_ppt(path: str) -> dict:
    """Parse a PPT/PPTX file into a basic research memory structure."""
    return {
        "source": str(Path(path)),
        "problem": None,
        "method": None,
        "experiments": [],
        "figures": [],
        "references": [],
    }
