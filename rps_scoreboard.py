import random

choices = ["rock", "paper", "scissors"]

wins = 0
losses = 0
draws = 0

print("===== ROCK PAPER SCISSORS =====")
print("Type 'quit' to stop playing.")

while True:
    player = input("\nChoose rock, paper, or scissors: ").lower().strip()

    if player == "quit":
        break

    if player not in choices:
        print("Invalid choice. Try again!")
        continue

    computer = random.choice(choices)

    print("You chose:", player)
    print("Computer chose:", computer)

    if player == computer:
        print("It's a draw!")
        draws += 1
    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("You win!")
        wins += 1
    else:
        print("You lose!")
        losses += 1

    print(f"Score: Wins={wins}, Losses={losses}, Draws={draws}")

print("\n===== FINAL SCOREBOARD =====")
print("Wins:", wins)
print("Losses:", losses)
print("Draws:", draws)
print("Thanks for playing!")
```
