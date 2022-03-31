from abc import ABC, abstractmethod, abstractclassmethod

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # Avoids cyclic imports for type hints
    from .Device import Device


class Configuration(ABC):
    @abstractmethod
    def apply(self, device: "Device"):
        raise NotImplementedError("Subclass should implement this")

    @abstractclassmethod
    def get(cls, device: "Device"):
        raise NotImplementedError("Subclass should implement this")
