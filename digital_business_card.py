print("===== DIGITAL BUSINESS CARD =====")

name = input("Enter your name: ")
role = input("Enter your profession: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")
github = input("Enter your GitHub username: ")

print("\n" + "=" * 35)
print("       DIGITAL BUSINESS CARD")
print("=" * 35)

print(f"Name       : {name}")
print(f"Profession : {role}")
print(f"Email      : {email}")
print(f"Phone      : {phone}")
print(f"GitHub     : github.com/{github}")

print("=" * 35)

# Save the card to a text file
with open("business_card.txt", "w") as file:
    file.write("DIGITAL BUSINESS CARD\n")
    file.write("=" * 30 + "\n")
    file.write(f"Name: {name}\n")
    file.write(f"Profession: {role}\n")
    file.write(f"Email: {email}\n")
    file.write(f"Phone: {phone}\n")
    file.write(f"GitHub: github.com/{github}\n")

print("\nBusiness card saved successfully!")
```
