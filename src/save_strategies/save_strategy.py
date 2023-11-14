from abc import ABC, abstractmethod
from typing import Any

class SaveStrategy(ABC):
    @abstractmethod
    def save(self, plot: Any):
        pass
