questions = {
    "Which language is used for Python programming?": {
        "a": "Python",
        "b": "HTML",
        "c": "CSS",
        "answer": "a"
    },
    "Which data type stores True or False?": {
        "a": "String",
        "b": "Boolean",
        "c": "List",
        "answer": "b"
    },
    "Which keyword defines a function in Python?": {
        "a": "function",
        "b": "define",
        "c": "def",
        "answer": "c"
    }
}

score = 0

print("=== Python Quiz Game ===")

for question, options in questions.items():
    print("\n" + question)
    print("a)", options["a"])
    print("b)", options["b"])
    print("c)", options["c"])

    answer = input("Your answer (a/b/c): ").lower()

    if answer == options["answer"]:
        print("Correct! 🎉")
        score += 1
    else:
        print("Wrong answer!")

print("\n=== Quiz Result ===")
print("Your score:", score, "/", len(questions))

if score == len(questions):
    print("Excellent! Perfect score!")
elif score >= 2:
    print("Good job!")
else:
    print("Keep practicing!")
