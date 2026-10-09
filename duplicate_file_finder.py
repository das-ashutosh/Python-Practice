files = [
    "notes.txt",
    "photo.jpg",
    "assignment.pdf",
    "notes.txt",
    "report.docx",
    "photo.jpg",
    "project.py"
]

seen = set()
duplicates = set()

for filename in files:
    if filename in seen:
        duplicates.add(filename)
    else:
        seen.add(filename)

print("All files:")
for filename in files:
    print("-", filename)

print("\nDuplicate files:")

if duplicates:
    for filename in sorted(duplicates):
        print("-", filename)
else:
    print("No duplicates found.")
