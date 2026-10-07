email = input("Enter your email address: ")
if "@" in email and "." in email:
    print("✅ Email format looks valid!")
else:
    print("❌ Invalid email format.")
