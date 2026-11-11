sentence = input("Enter a sentence: ")

words = sentence.split()

print("\n===== WORD LENGTH COUNTER =====")

for word in words:
    print(word, "=", len(word), "characters")

print("\nTotal Words:", len(words))
