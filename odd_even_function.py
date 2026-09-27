def check_number(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
number = int(input("Enter a number: "))
result = check_number(number)
print("The number is:", result)
