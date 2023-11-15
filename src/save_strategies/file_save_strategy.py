from typing import Any
from .save_strategy import SaveStrategy

class FileSaveStrategy(SaveStrategy):
    path: str

    def __init__(self, path: str):
        self.path = path

    def save(self, plot: Any):
        plot.savefig(self.path)
