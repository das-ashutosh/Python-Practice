number = int(input("Enter a number (1-100): "))
values = [
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I")
]
if 1 <= number <= 100:
    roman = ""

    for value, symbol in values:
        while number >= value:
            roman += symbol
            number -= value
    print("Roman Numeral:", roman)
else:
    print("Please enter a number between 1 and 100.")
