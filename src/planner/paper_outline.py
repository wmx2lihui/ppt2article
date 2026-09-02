"""Paper outline planner.

Transforms research memory into a manuscript structure.
"""


def build_outline(memory):
    return {
        "title": "",
        "abstract": "",
        "sections": [
            "Introduction",
            "Methodology",
            "Results",
            "Discussion",
            "Conclusion",
        ],
        "source_memory": memory,
    }
