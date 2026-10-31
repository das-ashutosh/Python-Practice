print("===== WEATHER REPORT GENERATOR =====")

try:
    temperature = float(input("Enter temperature in Celsius: "))

    print("\n===== WEATHER REPORT =====")
    print(f"Temperature: {temperature}°C")

    if temperature >= 35:
        condition = "Very Hot"
        advice = "Stay hydrated and avoid direct sunlight."

    elif temperature >= 25:
        condition = "Warm"
        advice = "Wear light and comfortable clothes."

    elif temperature >= 15:
        condition = "Pleasant"
        advice = "Enjoy your day!"

    elif temperature >= 5:
        condition = "Cold"
        advice = "Wear warm clothes."

    else:
        condition = "Very Cold"
        advice = "Stay warm and take care!"

    print("Weather:", condition)
    print("Suggestion:", advice)

except ValueError:
    print("Please enter a valid temperature.")

print("\nThank you for using the weather app!")
```
