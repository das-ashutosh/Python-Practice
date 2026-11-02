books = []
print("===== MINI LIBRARY SYSTEM =====")
while True:
    print("\n1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter book name: ").strip()

        if name:
            books.append({"name": name, "available": True})
            print("Book added successfully!")
        else:
            print("Book name cannot be empty.")

    elif choice == "2":
        print("\n===== BOOK LIST =====")

        if not books:
            print("No books available.")
        else:
            for i, book in enumerate(books, start=1):
                status = "Available" if book["available"] else "Borrowed"
                print(f"{i}. {book['name']} - {status}")

    elif choice == "3":
        name = input("Enter book name to borrow: ").strip()

        found = False

        for book in books:
            if book["name"].lower() == name.lower():
                found = True

                if book["available"]:
                    book["available"] = False
                    print("Book borrowed successfully!")
                else:
                    print("This book is already borrowed.")
                break

        if not found:
            print("Book not found.")

    elif choice == "4":
        name = input("Enter book name to return: ").strip()

        found = False

        for book in books:
            if book["name"].lower() == name.lower():
                found = True

                if not book["available"]:
                    book["available"] = True
                    print("Book returned successfully!")
                else:
                    print("This book was not borrowed.")
                break

        if not found:
            print("Book not found.")

    elif choice == "5":
        print("Thank you for using the library system!")
        break

    else:
        print("Invalid choice. Try again.")
