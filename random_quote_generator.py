import random

quotes = [
    ("Great things take time.", "Unknown"),
    ("Success is the sum of small efforts.", "Robert Collier"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("Learning never exhausts the mind.", "Leonardo da Vinci"),
    ("Dream big and start small.", "Unknown"),
    ("Code, learn, repeat.", "Developer Motto"),
    ("Every expert was once a beginner.", "Unknown")
]

print("=" * 35)
print("       RANDOM QUOTE GENERATOR")
print("=" * 35)

quote, author = random.choice(quotes)

print("\nYour quote for today:\n")
print(f'"{quote}"')
print(f"\n— {author}")

print("\nKeep learning and keep growing!")
```
