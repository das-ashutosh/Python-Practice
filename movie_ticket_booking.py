total_seats = 20
booked_seats = 0
ticket_price = 150

print("===== MOVIE TICKET BOOKING =====")

while True:
    print("\n1. View available seats")
    print("2. Book tickets")
    print("3. View booking summary")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        available = total_seats - booked_seats
        print("Available seats:", available)

    elif choice == "2":
        try:
            quantity = int(input("How many tickets? "))

            available = total_seats - booked_seats

            if quantity <= 0:
                print("Enter a valid ticket quantity.")

            elif quantity > available:
                print("Not enough seats available.")

            else:
                booked_seats += quantity
                amount = quantity * ticket_price

                print("\nBooking successful!")
                print("Tickets booked:", quantity)
                print("Total amount: Rs.", amount)

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "3":
        print("\n===== BOOKING SUMMARY =====")
        print("Total seats:", total_seats)
        print("Booked seats:", booked_seats)
        print("Available seats:", total_seats - booked_seats)
        print("Total revenue: Rs.", booked_seats * ticket_price)

    elif choice == "4":
        print("Thank you for using our booking system!")
        break

    else:
        print("Invalid option. Please try again.")
```
