"""Submission package builder MVP.

Collect manuscript, figures, tables, bibliography and supplementary files.
"""


class SubmissionPackageBuilder:
    def build_manifest(self, files):
        return {"files": files, "status": "initialized"}
