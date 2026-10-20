def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1
    steps = 0

    while left <= right:
        steps += 1
        middle = (left + right) // 2

        print(f"\nStep {steps}")
        print(f"Search range: {numbers[left:right + 1]}")
        print(f"Middle index: {middle}")
        print(f"Middle value: {numbers[middle]}")

        if numbers[middle] == target:
            print(f"\nFound {target} at index {middle}!")
            print(f"Total steps: {steps}")
            return middle

        elif numbers[middle] < target:
            print(f"{target} is larger. Search the right half.")
            left = middle + 1

        else:
            print(f"{target} is smaller. Search the left half.")
            right = middle - 1

    print(f"\n{target} was not found in the list.")
    print(f"Total steps: {steps}")
    return -1


print("===== BINARY SEARCH VISUALIZER =====")

try:
    numbers = list(map(
        int,
        input("Enter sorted numbers separated by spaces: ").split()
    ))

    if not numbers:
        print("Please enter at least one number.")
    elif numbers != sorted(numbers):
        print("Please enter numbers in ascending order.")
    else:
        target = int(input("Enter the number to find: "))
        binary_search(numbers, target)

except ValueError:
    print("Invalid input. Please enter whole numbers.")
```
