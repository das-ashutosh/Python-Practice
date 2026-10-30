import random

print("===== DICE ROLLING SIMULATOR =====")

while True:
    choice = input("\nRoll the dice? (yes/no): ").lower().strip()

    if choice == "no":
        print("Thanks for playing!")
        break

    elif choice == "yes":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("\nDice 1:", dice1)
        print("Dice 2:", dice2)
        print("Total:", dice1 + dice2)

        if dice1 == dice2:
            print("Amazing! You got a double!")

    else:
        print("Please enter yes or no.")
