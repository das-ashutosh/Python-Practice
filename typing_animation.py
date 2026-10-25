import time
import sys

def type_text(text, speed=0.05):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)
    print()

print("===== TYPING ANIMATION =====\n")

type_text("Hello, Python Developer!", 0.08)
type_text("Welcome to my GitHub profile.", 0.06)
type_text("Keep learning. Keep building. 🚀", 0.07)

print("\nAnimation finished!")
```
