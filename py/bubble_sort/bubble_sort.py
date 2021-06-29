from typing import List
from sort_strategy import SortStrategy

class BubbleSortStrategy(SortStrategy):
    view_array = []
    sorted_array = []

    def __init__(self, array: List[any]) -> None:
        super().__init__(array)
    
    def __next__(self):
        # Trivial cases
        if self.initial_array == []:
            raise StopIteration
        
        if len(self.initial_array) == 1:
            raise StopIteration

        # Stop
        if len(self.sorted_array) == len(self.initial_array):
            raise StopIteration
        
        if self.view_array == []:
            self.view_array = self.initial_array
            return self.view_array

        for idx, element in enumerate(self.view_array):
            if idx == len(self.view_array) - 1:
                # When the array is sorted
                self.sorted_array = self.view_array
                raise StopIteration

            next_element = self.view_array[idx + 1]
            if element > next_element:
                # If elements in the wrong order are found, swap them
                print(f"Found elements {element} and {next_element} at index {idx} in wrong order")
                self.view_array[idx] = next_element
                self.view_array[idx + 1] = element
                return self.view_array
