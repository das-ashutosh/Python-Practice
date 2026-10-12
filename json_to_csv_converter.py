import json
import csv

input_file = input("Enter JSON file name: ")
output_file = "converted_data.csv"

try:
    with open(input_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list) or not data:
        print("JSON must contain a non-empty list of objects.")
    elif not all(isinstance(item, dict) for item in data):
        print("Each item in the JSON list must be an object.")
    else:
        headers = list(dict.fromkeys(
            key for item in data for key in item
        ))

        with open(output_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)

        print("Conversion successful!")
        print("Output saved as:", output_file)

except FileNotFoundError:
    print("JSON file not found!")
except json.JSONDecodeError:
    print("Invalid JSON format!")
except OSError as error:
    print("File error:", error)
