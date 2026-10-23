```python
import random


def bubble_sort(data):
    arr = data.copy()
    comparisons = 0
    swaps = 0

    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            comparisons += 1

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return arr, comparisons, swaps


def selection_sort(data):
    arr = data.copy()
    comparisons = 0
    swaps = 0

    for i in range(len(arr)):
        smallest = i

        for j in range(i + 1, len(arr)):
            comparisons += 1

            if arr[j] < arr[smallest]:
                smallest = j

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            swaps += 1

    return arr, comparisons, swaps


def insertion_sort(data):
    arr = data.copy()
    comparisons = 0
    shifts = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break

        arr[j + 1] = key

    return arr, comparisons, shifts


def main():
    try:
        size = int(input("How many numbers? "))

        if not 1 <= size <= 1000:
            print("Choose a size between 1 and 1000.")
            return

        numbers = random.sample(range(1, size * 10 + 1), size)

        print("\nOriginal list:", numbers)

        algorithms = [
            ("Bubble Sort", bubble_sort),
            ("Selection Sort", selection_sort),
            ("Insertion Sort", insertion_sort)
        ]

        print("\n===== SORTING RACE =====")

        for name, algorithm in algorithms:
            result, comparisons, swaps = algorithm(numbers)

            print(f"\n{name}")
            print("Sorted:", result)
            print("Comparisons:", comparisons)
            print("Swaps/shifts:", swaps)

    except ValueError:
        print("Please enter a valid whole number.")


if __name__ == "__main__":
    main()
```
