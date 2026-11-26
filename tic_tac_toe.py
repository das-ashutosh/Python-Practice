 board = [" "] * 9
player = "X"

def display():
    print()
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))
        if i < 6:
            print("-----")

def winner():
    combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in combinations:
        if board[a] == board[b] == board[c] != " ":
            return True
    return False

for turn in range(9):
    display()
    print("Player", player)

    try:
        position = int(input("Choose position (1-9): ")) - 1
    except ValueError:
        print("Enter a valid number")
        continue

    if position < 0 or position > 8 or board[position] != " ":
        print("Invalid position")
        continue

    board[position] = player

    if winner():
        display()
        print("Player", player, "wins!")
        break

    player = "O" if player == "X" else "X"

else:
    display()
    print("Match Draw!")
