print("=== Markdown Table Generator ===")
headers = input("Enter column names separated by commas: ").split(",")
rows = int(input("How many rows do you want? "))
headers = [header.strip() for header in headers]
print("\nGenerated Markdown Table:\n")
print("| " + " | ".join(headers) + " |")
print("| " + " | ".join(["---"] * len(headers)) + " |")
for i in range(rows):
    values = input(
        f"Enter values for row {i + 1}, separated by commas: "
    ).split(",")
    values = [value.strip() for value in values]
    while len(values) < len(headers):
        values.append("")
    values = values[:len(headers)]
    print("| " + " | ".join(values) + " |")
