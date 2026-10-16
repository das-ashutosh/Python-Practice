```python
# Student Flashcard App

flashcards = {
    "What does CPU stand for?": "Central Processing Unit",
    "What is the extension of a Python file?": ".py",
    "What does RAM stand for?": "Random Access Memory",
    "What is 2 ** 3 in Python?": "8",
    "Which keyword defines a function in Python?": "def"
}

score = 0

print("===== STUDENT FLASHCARDS =====")
print("Answer the following questions!\n")

for question, answer in flashcards.items():
    print("Question:", question)
    user_answer = input("Your answer: ").strip()

    if user_answer.lower() == answer.lower():
        print("Correct! 🎉\n")
        score += 1
    else:
        print("Incorrect.")
        print("Correct answer:", answer, "\n")

print("===== FINAL RESULT =====")
print(f"Your score: {score}/{len(flashcards)}")
print(f"Percentage: {score / len(flashcards) * 100:.1f}%")

if score == len(flashcards):
    print("Excellent! You got everything right!")
elif score >= 3:
    print("Good job! Keep practicing.")
else:
    print("Keep revising. You will improve!")
```
