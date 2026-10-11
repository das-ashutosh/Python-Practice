import csv

input_file = input("Enter CSV file name: ")
output_file = "cleaned_data.csv"

try:
    with open(input_file, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if not rows:
        print("The CSV file is empty.")
    else:
        header = rows[0]
        unique_rows = list(dict.fromkeys(rows[1:]))

        with open(output_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(unique_rows)

        print("Original data rows:", len(rows) - 1)
        print("Cleaned data rows:", len(unique_rows))
        print("Removed duplicates:", len(rows) - 1 - len(unique_rows))
        print("Saved cleaned data to:", output_file)

except FileNotFoundError:
    print("CSV file not found!")

except (OSError, csv.Error) as error:
    print("Could not process the CSV file:", error)
