from PIL import Image
import os

filename = input("Enter image file path: ")

if os.path.exists(filename):
    try:
        with Image.open(filename) as image:
            print("\n=== Image Information ===")
            print("File name:", os.path.basename(filename))
            print("Format:", image.format)
            print("Width:", image.width, "pixels")
            print("Height:", image.height, "pixels")
            print("Color mode:", image.mode)
            print("File size:", os.path.getsize(filename), "bytes")
    except Exception:
        print("Unable to read this image.")
else:
    print("File not found!")
