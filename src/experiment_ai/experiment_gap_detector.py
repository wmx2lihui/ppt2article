"""Experiment gap detector interface for ppt2article v3.2."""


class ExperimentGapDetector:
    def analyze(self, manuscript):
        return {
            "missing_experiments": [],
            "reviewer_risks": [],
            "suggestions": [],
        }
