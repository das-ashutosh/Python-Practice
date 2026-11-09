password = input("Enter your password: ")

uppercase = 0
lowercase = 0
digits = 0
special = 0

for char in password:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        digits += 1
    else:
        special += 1

print("\n===== PASSWORD ANALYSIS =====")
print("Uppercase Letters:", uppercase)
print("Lowercase Letters:", lowercase)
print("Digits:", digits)
print("Special Characters:", special)
print("Total Characters:", len(password))
