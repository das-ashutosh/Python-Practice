import getpass

PASSWORD = "python123"
FILE_NAME = "private_notes.txt"

entered_password = getpass.getpass("Enter password: ")

if entered_password == PASSWORD:
    print("\n1. Write a note")
    print("2. Read saved notes")

    choice = input("Choose an option: ")

    if choice == "1":
        note = input("Write your note: ")

        with open(FILE_NAME, "a", encoding="utf-8") as file:
            file.write(note + "\n")

        print("Note saved successfully!")

    elif choice == "2":
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                print("\nYour notes:\n")
                print(file.read())
        except FileNotFoundError:
            print("No notes found yet.")

    else:
        print("Invalid option.")

else:
    print("Incorrect password!")
