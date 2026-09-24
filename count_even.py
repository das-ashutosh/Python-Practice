numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)
count = 0
for num in numbers:
    if num % 2 == 0:
        count += 1
print("Number of even numbers:", count)
