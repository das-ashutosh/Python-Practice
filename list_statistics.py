numbers = input("Enter numbers separated by spaces: ")

numbers = [int(x) for x in numbers.split()]

total = sum(numbers)
average = total / len(numbers)

print("\n===== LIST STATISTICS =====")
print("Numbers:", numbers)
print("Sum:", total)
print("Average:", average)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
