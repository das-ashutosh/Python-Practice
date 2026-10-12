import zipfile
import os

print("=== ZIP File Creator ===")

files_input = input(
    "Enter file paths separated by commas: "
)

files = [name.strip() for name in files_input.split(",")]
zip_name = input("Enter output ZIP name: ").strip()

if not zip_name.endswith(".zip"):
    zip_name += ".zip"

try:
    with zipfile.ZipFile(
        zip_name, "w", compression=zipfile.ZIP_DEFLATED
    ) as archive:
        for filename in files:
            if os.path.isfile(filename):
                archive.write(filename, arcname=os.path.basename(filename))
                print("Added:", filename)
            else:
                print("File not found:", filename)

    print("\nZIP archive created:", zip_name)

except (OSError, zipfile.BadZipFile) as error:
    print("Could not create ZIP:", error)
