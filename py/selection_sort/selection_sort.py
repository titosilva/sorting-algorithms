from typing import List
from sort_strategy import SortStrategy

class SelectionSortStrategy(SortStrategy):
    view_array = []
    sorted_array = []
    current_index = 0

    def __init__(self, array: List[any]) -> None:
        super().__init__(array)

    def __go_to_next(self):
        self.view_array = []
        self.current_index += 1
        if self.current_index == len(self.initial_array):
            raise StopIteration

        print("Selected element: " + str(self.initial_array[self.current_index-1]))
    
    def __next__(self):
        # Trivial cases
        if self.initial_array == []:
            raise StopIteration
        
        if len(self.initial_array) == 1:
            raise StopIteration

        if len(self.sorted_array) == len(self.initial_array):
            raise StopIteration
        
        if self.view_array == []:
            self.view_array = self.initial_array
            return self.view_array
        
        print("\nSearching for minimum in the elements that are not sorted:\n" + str(self.view_array))
        minimum = min(self.view_array)
        position = self.view_array.index(minimum)
        print("The minimum is " + str(minimum))

        self.sorted_array.append(minimum)
        self.view_array[position] = self.view_array[0]
        self.view_array = self.view_array[1:]

        print("Swapping the minimum with the first element that is not sorted...")
        return self.sorted_array + self.view_array