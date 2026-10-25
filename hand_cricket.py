import random

print("===== HAND CRICKET =====")
print("Choose runs from 1 to 6.")
print("If your run matches the computer's run, you're OUT!")

player_score = 0

while True:
    try:
        player = int(input("\nEnter your run (1-6): "))

        if player not in range(1, 7):
            print("Choose a number between 1 and 6.")
            continue

        computer = random.randint(1, 6)
        print("Computer chose:", computer)

        if player == computer:
            print("\nOUT!")
            break

        player_score += player
        print("Your score:", player_score)

    except ValueError:
        print("Please enter a valid number.")

print("\n===== MATCH RESULT =====")
print("Final score:", player_score)
print("Thanks for playing!")
```
