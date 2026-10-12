import json
from pathlib import Path

FILE_NAME = "bookmarks.json"


def load_bookmarks():
    if Path(FILE_NAME).exists():
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not read bookmarks. Starting fresh.")
    return []


def save_bookmarks(bookmarks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(bookmarks, file, indent=4)


bookmarks = load_bookmarks()

while True:
    print("\n=== Bookmark Manager ===")
    print("1. Add bookmark")
    print("2. View bookmarks")
    print("3. Search bookmarks")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Website title: ").strip()
        url = input("Website URL: ").strip()

        if title and url.startswith(("https://", "http://")):
            bookmarks.append({"title": title, "url": url})
            save_bookmarks(bookmarks)
            print("Bookmark saved!")
        else:
            print("Enter a title and a valid HTTP/HTTPS URL.")

    elif choice == "2":
        if not bookmarks:
            print("No bookmarks saved.")
        else:
            for number, item in enumerate(bookmarks, start=1):
                print(f"{number}. {item['title']} - {item['url']}")

    elif choice == "3":
        keyword = input("Search by title: ").strip().lower()
        matches = [
            item for item in bookmarks
            if keyword in item["title"].lower()
        ]

        for item in matches:
            print(item["title"], "-", item["url"])

        if not matches:
            print("No matching bookmarks found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
