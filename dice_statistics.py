import random

rolls = int(input("How many times do you want to roll the dice? "))
results = []
for i in range(rolls):
    results.append(random.randint(1, 6))
print("\n🎲 Dice Results:")
print(results)
print("\nStatistics:")
for number in range(1, 7):
    count = results.count(number)
    print(number, "appeared", count, "time(s)")
print("\nTotal rolls:", rolls)
