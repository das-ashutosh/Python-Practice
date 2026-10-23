```python
from PIL import Image

def convert_to_ascii(image_path, width=80):
    characters = "@%#*+=-:. "

    image = Image.open(image_path).convert("L")

    # Preserve the image's approximate aspect ratio
    height = int(image.height * width / image.width / 2)
    image = image.resize((width, max(1, height)))

    pixels = list(image.getdata())
    ascii_art = ""

    for row in range(image.height):
        for col in range(image.width):
            brightness = pixels[row * image.width + col]
            index = brightness * (len(characters) - 1) // 256
            ascii_art += characters[index]
        ascii_art += "\n"

    return ascii_art


def main():
    print("===== IMAGE TO ASCII CONVERTER =====")
    image_path = input("Enter image path: ").strip()

    try:
        art = convert_to_ascii(image_path)

        print("\n" + art)

        with open("ascii_art.txt", "w", encoding="utf-8") as file:
            file.write(art)

        print("ASCII art saved to ascii_art.txt")

    except FileNotFoundError:
        print("Image file not found. Check the path.")
    except Exception as error:
        print("Could not process image:", error)


if __name__ == "__main__":
    main()
```
