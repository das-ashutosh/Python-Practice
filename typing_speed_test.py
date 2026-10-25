import time
import random

sentences = [
    "Python makes programming fun and simple.",
    "Practice every day to improve your coding skills.",
    "Small projects help you become a better developer.",
    "Learning algorithms improves logical thinking."
]

print("===== TYPING SPEED TEST =====")
print("Type the sentence as quickly and accurately as possible.\n")

sentence = random.choice(sentences)
print("Sentence:", sentence)

input("\nPress Enter when you are ready...")

start = time.time()
typed_text = input("\nStart typing: ")
end = time.time()

elapsed = end - start
minutes = elapsed / 60

words = len(typed_text.split())
wpm = words / minutes if minutes > 0 else 0

correct_chars = sum(
    1 for a, b in zip(typed_text, sentence) if a == b
)
accuracy = (
    correct_chars / len(sentence) * 100
    if sentence else 0
)

print("\n===== YOUR RESULTS =====")
print(f"Time taken: {elapsed:.2f} seconds")
print(f"Typing speed: {wpm:.2f} WPM")
print(f"Character accuracy: {accuracy:.2f}%")
```
