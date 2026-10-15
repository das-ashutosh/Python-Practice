from pathlib import Path
import difflib

print("=== Text File Comparator ===")

file1 = input("Enter first file path: ").strip()
file2 = input("Enter second file path: ").strip()

try:
    text1 = Path(file1).read_text(encoding="utf-8").splitlines()
    text2 = Path(file2).read_text(encoding="utf-8").splitlines()

    changes = list(difflib.unified_diff(
        text1,
        text2,
        fromfile=file1,
        tofile=file2,
        lineterm=""
    ))

    if changes:
        print("\n=== Differences ===")
        for line in changes:
            print(line)
    else:
        print("\nBoth files are identical!")

except FileNotFoundError:
    print("One of the files could not be found.")
except (OSError, UnicodeError) as error:
    print("Could not compare files:", error)
