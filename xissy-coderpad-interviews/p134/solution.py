import abc
from typing import List


class SparseArrayInterface:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def init(self, arr: List[int], size: int):
        """
        initialize with the original large array and size
        """
        pass

    @abc.abstractmethod
    def set(self, i: int, val: int):
        """
        updates index at i with val
        """
        pass

    @abc.abstractmethod
    def get(self, i: int) -> int:
        """
        gets the value at index i
        """
        pass


class SparseArray(SparseArrayInterface):
    def init(self, arr: List[int], size: int):
        pass

    def set(self, i: int, val: int):
        # TODO: solve
        pass

    def get(self, i: int) -> int:
        # TODO: solve
        return 0
