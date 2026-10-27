```python
# Secret Message Vault

print("===== SECRET MESSAGE VAULT =====")

password = "python123"
secret_message = "Keep learning and never give up!"

attempts = 3

while attempts > 0:
    entered_password = input("Enter your password: ")

    if entered_password == password:
        print("\nAccess granted!")
        print("Your secret message:")
        print(secret_message)
        break

    attempts -= 1
    print("Incorrect password.")

    if attempts > 0:
        print("Attempts remaining:", attempts)

if attempts == 0:
    print("Access denied. Try again later.")
```

