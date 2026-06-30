from abc import ABC, abstractmethod
from pathlib import Path


class BaseParser(ABC):
    """
    Abstract parser for all document types.
    """

    @abstractmethod
    def parse(self, file_path: Path) -> str:
        pass