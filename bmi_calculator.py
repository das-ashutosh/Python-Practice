weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height * height)

print("Your BMI is:", round(bmi, 2))
