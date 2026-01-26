from typing import Any
from .save_strategy import SaveStrategy
from utils import get_image_metadata

class FileSaveStrategy(SaveStrategy):
    path: str

    def __init__(self, path: str):
        self.path = path

    def save(self, name: str, plot: Any):
        path = f'{self.path}{name}'

        plot.savefig(path, metadata=get_image_metadata())
