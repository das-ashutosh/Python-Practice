rows = int(input("Enter number of rows: "))

triangle = []

for i in range(rows):
    current = [1]

    for j in range(1, i):
        value = triangle[i-1][j-1] + triangle[i-1][j]
        current.append(value)

    if i > 0:
        current.append(1)

    triangle.append(current)

print("Pascal's Triangle:")

for row in triangle:
    print(" ".join(map(str, row)).center(rows * 3))
