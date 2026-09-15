principal = float(input("Enter principal: "))
rate = float(input("Enter rate (%): "))
time = float(input("Enter time (years): "))

interest = (principal * rate * time) / 100

print("Simple interest:", interest)
