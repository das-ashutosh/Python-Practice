from datetime import datetime
print("=== Personal Journal ===")
entry = input("Write about your day: ")
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("journal.txt", "a", encoding="utf-8") as file:
    file.write(f"\n[{date}]\n")
    file.write(entry + "\n")
    file.write("-" * 40 + "\n")

print("\nYour journal entry has been saved!")
