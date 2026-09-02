"""
Scientific figure caption generation module.

Captions should explain observation, mechanism and significance.
"""


class CaptionGenerator:
    def generate(self, figure_info):
        return {
            "caption": "",
            "observation": figure_info.get("observation"),
            "interpretation": figure_info.get("interpretation"),
        }
