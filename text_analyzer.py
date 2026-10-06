text = input("Enter a sentence: ")
words = text.split()
characters = len(text)
vowels = 0
for char in text.lower():
    if char in "aeiou":
        vowels += 1

print("\n📊 Text Analysis")
print("Words:", len(words))
print("Characters:", characters)
print("Vowels:", vowels)
