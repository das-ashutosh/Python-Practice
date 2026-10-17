```python
# Sudoku Puzzle Validator

def is_valid_sudoku(board):
    # Check rows
    for row in board:
        numbers = [n for n in row if n != 0]
        if len(numbers) != len(set(numbers)):
            return False

    # Check columns
    for col in range(9):
        numbers = [
            board[row][col]
            for row in range(9)
            if board[row][col] != 0
        ]
        if len(numbers) != len(set(numbers)):
            return False

    # Check each 3x3 box
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            numbers = []

            for r in range(box_row, box_row + 3):
                for c in range(box_col, box_col + 3):
                    value = board[r][c]
                    if value != 0:
                        numbers.append(value)

            if len(numbers) != len(set(numbers)):
                return False

    return True


# 0 represents an empty cell
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("===== SUDOKU VALIDATOR =====")

for row in board:
    print(" ".join(str(n) if n != 0 else "." for n in row))

if is_valid_sudoku(board):
    print("\nThe Sudoku board is valid so far!")
else:
    print("\nThe Sudoku board contains a rule violation.")
```
