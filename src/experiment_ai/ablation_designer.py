"""Ablation experiment planner interface for ppt2article."""


class AblationDesigner:
    def design(self, modules):
        return {
            "ablations": [],
            "purpose": "Validate contribution of each component.",
        }
