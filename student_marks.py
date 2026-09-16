marks = []

for i in range(3):
    mark = float(input("Enter marks: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

print("Total marks:", total)
print("Average marks:", round(average, 2))
