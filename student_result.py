name = input("Enter student name: ")
maths = int(input("Enter Maths marks: "))
python = int(input("Enter Python marks: "))
english = int(input("Enter English marks: "))
total = maths + python + english
percentage = total / 3
print("\n--- Student Result ---")
print("Name:", name)
print("Total:", total)
print("Percentage:", round(percentage, 2))
