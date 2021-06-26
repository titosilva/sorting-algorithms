from typing import List
from sort_strategy import SortStrategy

class InsertionSortStrategy(SortStrategy):
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

        print("Inserted element: " + str(self.initial_array[self.current_index-1]))
    
    def __next__(self):
        # Trivial cases
        if self.initial_array == []:
            return []
        
        if len(self.initial_array) == 1:
            return self.initial_array

        if len(self.sorted_array) == len(self.initial_array):
            return self.sorted_array

        if self.view_array == []:
            self.view_array = [self.sorted_array, self.initial_array[self.current_index], []]
            print("\nInserting next element: " + str(self.initial_array[self.current_index]))
            return self.view_array

        should_be_minor_than_element = self.view_array[0]
        element = self.view_array[1]
        are_greater_than_element = self.view_array[2]

        if len(should_be_minor_than_element) == 0:
            self.sorted_array = [element] + are_greater_than_element
            self.__go_to_next()
            return self.sorted_array
        else:
            may_be_greater = should_be_minor_than_element.pop()

            if may_be_greater > element:
                are_greater_than_element.insert(0, may_be_greater)
                self.view_array = [should_be_minor_than_element, element, are_greater_than_element]
            else:
                self.sorted_array = should_be_minor_than_element + [may_be_greater, element] + are_greater_than_element
                self.__go_to_next()
                return self.sorted_array
        
        return self.view_array
        


        
