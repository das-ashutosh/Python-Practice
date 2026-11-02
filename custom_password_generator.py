import random
import string

print("===== CUSTOM PASSWORD GENERATOR =====")

try:
    length = int(input("Enter password length: "))

    if length < 4:
        print("Password length must be at least 4.")

    else:
        characters = ""

        upper = input("Include uppercase letters? (y/n): ").lower()
        lower = input("Include lowercase letters? (y/n): ").lower()
        digits = input("Include numbers? (y/n): ").lower()
        symbols = input("Include special characters? (y/n): ").lower()

        if upper == "y":
            characters += string.ascii_uppercase

        if lower == "y":
            characters += string.ascii_lowercase

        if digits == "y":
            characters += string.digits

        if symbols == "y":
            characters += "!@#$%^&*"

        if not characters:
            print("Please select at least one character type.")

        else:
            password = "".join(
                random.choice(characters)
                for _ in range(length)
            )

            print("\nGenerated Password:", password)

except ValueError:
    print("Please enter a valid number.")
