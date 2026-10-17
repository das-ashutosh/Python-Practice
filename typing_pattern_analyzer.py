```python
from collections import Counter
import string

print("===== TYPING PATTERN ANALYZER =====")

text = input("Enter a sentence: ")

if not text.strip():
    print("Please enter some text.")
else:
    letters = [
        char.lower()
        for char in text
        if char.isalpha()
    ]

    if letters:
        frequency = Counter(letters)

        print("\nTotal letters:", len(letters))
        print("Unique letters:", len(frequency))

        print("\nLetter frequencies:")
        for letter, count in sorted(frequency.items()):
            print(f"{letter}: {count} {'*' * count}")

        most_common = frequency.most_common(1)
        highest_count = most_common[0][1]

        common_letters = [
            letter for letter, count in frequency.items()
            if count == highest_count
        ]

        print("\nMost frequent letter(s):",
              ", ".join(common_letters))
        print("Frequency:", highest_count)
    else:
        print("No alphabetic letters found.")

    digits = sum(char.isdigit() for char in text)
    spaces = sum(char.isspace() for char in text)
    punctuation = sum(
        char in string.punctuation for char in text
    )

    print("\nDigits:", digits)
    print("Spaces:", spaces)
    print("Punctuation marks:", punctuation)
```
