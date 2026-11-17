filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        content = file.read()

    lines = content.splitlines()
    words = content.split()
    characters = len(content)

    print("\n===== FILE ANALYSIS =====")
    print("Total Lines:", len(lines))
    print("Total Words:", len(words))
    print("Total Characters:", characters)

except FileNotFoundError:
    print("File not found!")
