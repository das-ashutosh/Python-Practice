sentence = input("Enter a sentence: ")
word = input("Enter word to search: ")

words = sentence.lower().split()

if word.lower() in words:
    print("Word found in the sentence!")
else:
    print("Word not found!")
