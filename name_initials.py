name = input("Enter your full name: ")
words = name.split()
initials = ""
for word in words:
    initials += word[0].upper()
print("Your initials are:", initials)
