import abc
from typing import List

class SortStrategy(abc.ABC):
    initial_array = []

    def __init__(self, array: List[any]) -> None:
        super().__init__()
        self.initial_array = array

    def __iter__(self):
        return self

    @abc.abstractmethod
    def __next__(self):
        pass
