word = input("Enter a word: ")

if word.lower() == word.lower()[::-1]:
    print(word, "is a palindrome!")
else:
    print(word, "is not a palindrome.")
