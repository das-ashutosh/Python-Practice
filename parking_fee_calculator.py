import math

hours = float(input("Enter parking duration in hours: "))

if hours <= 0:
    print("Invalid parking duration")
else:
    total_hours = math.ceil(hours)

    if total_hours == 1:
        fee = 20
    else:
        fee = 20 + (total_hours - 1) * 10

    print("Total parking hours:", total_hours)
    print("Parking fee: Rs.", fee)
