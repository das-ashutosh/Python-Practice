```python
import random

def generate_maze(rows, cols):
    # Each cell starts as a wall
    maze = [["#" for _ in range(cols * 2 + 1)]
            for _ in range(rows * 2 + 1)]

    visited = set()

    def carve(r, c):
        visited.add((r, c))
        maze[r * 2 + 1][c * 2 + 1] = " "

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (0 <= nr < rows and
                0 <= nc < cols and
                (nr, nc) not in visited):

                maze[r + nr + 1][c + nc + 1] = " "
                carve(nr, nc)

    carve(0, 0)

    # Mark entrance and exit
    maze[1][0] = "S"
    maze[rows * 2 - 1][cols * 2] = "E"

    return maze


try:
    rows = int(input("Enter maze height (3-15): "))
    cols = int(input("Enter maze width (3-15): "))

    if not (3 <= rows <= 15 and 3 <= cols <= 15):
        print("Please enter values between 3 and 15.")
    else:
        maze = generate_maze(rows, cols)

        print("\n===== RANDOM MAZE =====")
        for line in maze:
            print("".join(line))

        print("\nS = Start | E = Exit | # = Wall")

except ValueError:
    print("Please enter whole numbers.")
```
