import re
from collections import Counter
print("=== Duplicate Word Highlighter ===")
text = input("Enter a paragraph: ").lower()
words = re.findall(r"\b[a-z0-9']+\b", text)
word_counts = Counter(words)
duplicates = {
    word: count
    for word, count in word_counts.items()
    if count > 1
}
if duplicates:
    print("\nRepeated words:")
    for word, count in sorted(duplicates.items()):
        print(f"{word}: {count} times")
else:
    print("\nNo repeated words found!")

print("\nTotal words:", len(words))
print("Unique words:", len(word_counts))
