"""Equation understanding interface for scientific manuscripts."""


class EquationParser:
    def parse(self, equation):
        return {
            "variables": [],
            "equation_type": None,
            "physical_meaning": None,
            "assumptions": [],
        }
