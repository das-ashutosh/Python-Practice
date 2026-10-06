contacts = {}
print("📱 Contact Book")
name = input("Enter contact name: ")
phone = input("Enter phone number: ")
contacts[name] = phone
print("\nContact saved successfully!")
print("\nYour Contacts:")
for name, phone in contacts.items():
    print(name, ":", phone)
