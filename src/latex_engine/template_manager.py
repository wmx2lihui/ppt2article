"""Journal LaTeX template management module.

MVP implementation for journal template selection.
"""


class TemplateManager:
    def __init__(self, journal=None):
        self.journal = journal

    def load_template(self):
        return {"journal": self.journal, "template": None}
