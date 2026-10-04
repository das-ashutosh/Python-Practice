password = input("Enter a password: ")
if len(password) >= 8:
    print("Password length is acceptable!")
else:
    print("Password is too short.")
    print("Use at least 8 characters.")
