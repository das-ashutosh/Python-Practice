score = 0
answer = input("What is the capital of India? ")
if answer.lower() == "new delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
answer = input("How many days are there in a week? ")
if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("Your score:", score, "/ 2")
