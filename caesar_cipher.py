message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted = ""

for char in message:
    if char.isupper():
        encrypted += chr((ord(char) - 65 + shift) % 26 + 65)
    elif char.islower():
        encrypted += chr((ord(char) - 97 + shift) % 26 + 97)
    else:
        encrypted += char

print("Encrypted message:", encrypted)
