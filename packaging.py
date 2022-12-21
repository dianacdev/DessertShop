"""Used to make a class abstract or a method"""
from abc import ABC, abstractmethod


class Packaging(ABC):
    """Package Interface"""
    @property
    @abstractmethod
    def packaging(self):
        """Getting the package type"""

    @packaging.setter
    @abstractmethod
    def packaging(self, package_type):
        pass

    @classmethod
    def __subclasshook__(cls, packaging):
        if cls is packaging:
            return True
        return False
