ones = [
    "Zero", "One", "Two", "Three", "Four",
    "Five", "Six", "Seven", "Eight", "Nine",
    "Ten", "Eleven", "Twelve", "Thirteen",
    "Fourteen", "Fifteen", "Sixteen",
    "Seventeen", "Eighteen", "Nineteen"
]

tens = [
    "", "", "Twenty", "Thirty", "Forty",
    "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
]

num = int(input("Enter a number (0-999): "))

if num < 0 or num > 999:
    print("Please enter a number between 0 and 999.")

elif num < 20:
    print(ones[num])

elif num < 100:
    print(tens[num // 10] +
          (" " + ones[num % 10] if num % 10 else ""))

else:
    result = ones[num // 100] + " Hundred"
    remainder = num % 100

    if remainder < 20 and remainder > 0:
        result += " " + ones[remainder]
    elif remainder >= 20:
        result += " " + tens[remainder // 10]

        if remainder % 10:
            result += " " + ones[remainder % 10]

    print(result)
