player_score = 0
computer_score = 0

player = input("Enter your choice (rock/paper/scissors): ")
computer = input("Enter computer choice: ")
if player == computer:
    print("It's a tie!")
elif (
    (player == "rock" and computer == "scissors")
    or (player == "paper" and computer == "rock")
    or (player == "scissors" and computer == "paper")
):
    print("You win!")
    player_score += 1
else:
    print("Computer wins!")
    computer_score += 1

print("Player score:", player_score)
print("Computer score:", computer_score)
