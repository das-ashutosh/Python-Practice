rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

matrix = []

print("Enter matrix elements:")

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

transpose = []

for j in range(cols):
    row = []
    for i in range(rows):
        row.append(matrix[i][j])
    transpose.append(row)

print("Transposed matrix:")

for row in transpose:
    print(row)
