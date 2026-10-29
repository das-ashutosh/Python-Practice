import os
from collections import Counter

print("===== FILE EXTENSION ANALYZER =====")

folder = input("Enter folder path: ").strip()

if not os.path.isdir(folder):
    print("Folder not found. Please check the path.")
else:
    extensions = []

    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)

        if os.path.isfile(filepath):
            extension = os.path.splitext(filename)[1].lower()

            if extension:
                extensions.append(extension)
            else:
                extensions.append("No extension")

    counts = Counter(extensions)

    if not counts:
        print("No files found in this folder.")
    else:
        print("\n===== EXTENSION REPORT =====")

        for extension, count in counts.most_common():
            print(f"{extension}: {count} file(s)")

        print("\nTotal files analyzed:", len(extensions))
        print("Different extension types:", len(counts))
```
