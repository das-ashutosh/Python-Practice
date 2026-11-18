num = int(input("Enter a number: "))
n = num
factors = []

if num < 2:
    print("Enter a number greater than 1")
else:
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1

    print("Prime factors of", num, "are:", factors)
