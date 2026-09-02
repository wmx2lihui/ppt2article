"""Figure analysis interface for ppt2article v2.7.

This module defines the interface for converting scientific figures
into structured research information.
"""


class FigureAnalyzer:
    def analyze(self, figure):
        return {
            "type": None,
            "scientific_role": None,
            "main_observation": None,
            "related_section": None,
        }
