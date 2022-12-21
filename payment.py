"""Used to make a class abstract or a method"""
from abc import ABC, abstractmethod
from enum import Enum

class Payment(ABC):
    """Payment Interface"""
    PayType = Enum('PayType', 'CASH CARD PHONE')

    @property
    @abstractmethod
    def pay_type(self):
        """Getting the paytype"""

    @pay_type.setter
    @abstractmethod
    def pay_type(self, new_pay_type):
        pass
