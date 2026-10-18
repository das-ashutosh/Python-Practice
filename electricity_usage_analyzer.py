```python
# Smart Electricity Usage Analyzer

def calculate_energy(power_watts, hours_per_day, days):
    return (power_watts * hours_per_day * days) / 1000


def main():
    appliances = []

    print("===== ELECTRICITY USAGE ANALYZER =====")
    print("Enter your appliance details.\n")

    while True:
        name = input("Appliance name (or 'done' to finish): ").strip()

        if name.lower() == "done":
            break

        try:
            power = float(input("Power rating (watts): "))
            hours = float(input("Hours used per day: "))
            days = int(input("Days used per month: "))

            if power <= 0 or hours < 0 or hours > 24 or not 1 <= days <= 31:
                print("Invalid values. Please try again.\n")
                continue

            energy = calculate_energy(power, hours, days)

            appliances.append({
                "name": name,
                "energy": energy
            })

            print(f"Monthly usage: {energy:.2f} kWh\n")

        except ValueError:
            print("Please enter valid numeric values.\n")

    if not appliances:
        print("No appliance data entered.")
        return

    rate = float(input("Electricity rate per kWh (₹): "))

    if rate < 0:
        print("Electricity rate cannot be negative.")
        return

    total_energy = sum(item["energy"] for item in appliances)
    total_cost = total_energy * rate

    print("\n===== MONTHLY REPORT =====")

    for item in sorted(
        appliances,
        key=lambda item: item["energy"],
        reverse=True
    ):
        cost = item["energy"] * rate
        print(
            f"{item['name']}: {item['energy']:.2f} kWh "
            f"| ₹{cost:.2f}"
        )

    print(f"\nTotal consumption: {total_energy:.2f} kWh")
    print(f"Estimated electricity cost: ₹{total_cost:.2f}")


if __name__ == "__main__":
    main()
```
