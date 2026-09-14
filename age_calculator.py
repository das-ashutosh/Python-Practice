from datetime import datetime
birth_year = int(input("Enter your birth year: "))
current_year = datetime.now().year

age = current_year - birth_year
print("Your approximate age is:", age)
