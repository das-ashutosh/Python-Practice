print("===== COLOR MIXER =====")

try:
    print("Enter RGB values from 0 to 255.")

    r1 = int(input("Color 1 - Red: "))
    g1 = int(input("Color 1 - Green: "))
    b1 = int(input("Color 1 - Blue: "))

    r2 = int(input("\nColor 2 - Red: "))
    g2 = int(input("Color 2 - Green: "))
    b2 = int(input("Color 2 - Blue: "))

    values = [r1, g1, b1, r2, g2, b2]

    if any(value < 0 or value > 255 for value in values):
        print("Error: RGB values must be between 0 and 255.")
    else:
        red = (r1 + r2) // 2
        green = (g1 + g2) // 2
        blue = (b1 + b2) // 2

        print("\n===== MIXED COLOR =====")
        print(f"Red: {red}")
        print(f"Green: {green}")
        print(f"Blue: {blue}")
        print(f"RGB: ({red}, {green}, {blue})")
        print(f"HEX: #{red:02X}{green:02X}{blue:02X}")

except ValueError:
    print("Please enter valid whole numbers.")
```
