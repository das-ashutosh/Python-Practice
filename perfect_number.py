num = int(input("Enter a number: "))

total = 0

for i in range(1, num):
    if num % i == 0:
        total += i

print("Sum of divisors:", total)

if num > 0 and total == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")
