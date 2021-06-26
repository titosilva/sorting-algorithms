from insertion_sort.insertion_sort import InsertionSortStrategy

def display_sorting():
    array = [5,4,2,1,3]
    strategy = InsertionSortStrategy(array)
    strategy_iterator = iter(strategy)
    strategy_result = []

    print("Sorting array " + str(array))
    while len(strategy_result) != len(array):
        try:
            strategy_result = next(strategy_iterator)
            print(strategy_result)
        except StopIteration:
            print("Sorting ended")

if __name__ == "__main__":
    display_sorting()