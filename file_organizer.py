from pathlib import Path
import shutil

def organize_files(folder_path):
    folder = Path(folder_path)

    if not folder.is_dir():
        print("Folder not found!")
        return

    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
        "Documents": [".pdf", ".docx", ".txt", ".doc"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Code": [".py", ".java", ".js", ".html", ".css"],
        "Audio": [".mp3", ".wav", ".aac"]
    }

    moved = 0

    for file in list(folder.iterdir()):
        if not file.is_file():
            continue

        category = "Others"

        for name, extensions in categories.items():
            if file.suffix.lower() in extensions:
                category = name
                break

        destination = folder / category
        destination.mkdir(exist_ok=True)

        target = destination / file.name

        if target.exists():
            print("Skipped duplicate:", file.name)
            continue

        shutil.move(str(file), str(target))
        print(f"Moved {file.name} -> {category}/")
        moved += 1

    print(f"\nOrganization complete! Files moved: {moved}")


path = input("Enter folder path to organize: ").strip()
organize_files(path)
