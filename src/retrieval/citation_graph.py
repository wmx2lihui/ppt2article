"""Citation graph placeholder for ppt2article v2.8.

Future implementation:
- construct paper relationship graph
- rank important references
- trace claim-evidence links
"""


class CitationGraph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_paper(self, paper):
        self.nodes.append(paper)

    def add_relation(self, source, target, relation):
        self.edges.append((source, target, relation))
