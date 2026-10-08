import random
words = ["python", "computer", "programming", "github", "developer"]
word = random.choice(words)
scrambled = list(word)
random.shuffle(scrambled)
scrambled_word = "".join(scrambled)
print("🔤 Word Scramble Game")
print("Unscramble this word:", scrambled_word)
guess = input("Your answer: ").lower()
if guess == word:
    print("🎉 Correct!")
else:
    print("❌ Wrong!")
    print("The correct word was:", word)
