"""Research memory storage for ppt2article MVP."""

import json
from pathlib import Path


class ResearchMemory:
    def __init__(self, data=None):
        self.data = data or {}

    def update(self, key, value):
        self.data[key] = value

    def save(self, path):
        Path(path).write_text(
            json.dumps(self.data, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    @classmethod
    def load(cls, path):
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        return cls(data)
