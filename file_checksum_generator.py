import hashlib
from pathlib import Path

def calculate_sha256(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


path = input("Enter file path: ").strip()
file_path = Path(path)

if file_path.is_file():
    checksum = calculate_sha256(file_path)

    print("\n=== File Checksum ===")
    print("File:", file_path.name)
    print("SHA-256:", checksum)
else:
    print("File not found. Please check the path.")
