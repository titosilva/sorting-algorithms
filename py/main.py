from sort_strategy import SortStrategy
from selection_sort.selection_sort import SelectionSortStrategy
from insertion_sort.insertion_sort import InsertionSortStrategy

def display_sorting(strategy: SortStrategy):
    strategy_iterator = iter(strategy)
    strategy_result = []

    print("Sorting array " + str(array))
    while True:
        try:
            strategy_result = next(strategy_iterator)
            print(strategy_result)
        except StopIteration:
            print("Sorting ended")
            break

algorithms = [
    {
        "name": "Insertion Sort",
        "strategy": InsertionSortStrategy,
    },
    {
        "name": "Selection Sort",
        "strategy": SelectionSortStrategy,
    },
]

if __name__ == "__main__":
    print("Available algorithms:")

    for idx, info in enumerate(algorithms):
        print(str(idx) + " - " + info["name"])


    while True:
        try:
            selected = int(input("Please, type a number: "))

            if idx < 0 or idx >= len(algorithms):
                print("Invalid input. Please, select one of the available algorithms.")
        except KeyboardInterrupt:
            break
        except:
            print("Invalid input.")

        array = [5,4,2,1,3]
        print("\n\nStrategy: "+algorithms[selected]["name"])
        display_sorting(algorithms[selected]["strategy"](array))
        print("\n")

        
