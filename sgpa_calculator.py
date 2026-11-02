print("===== SGPA CALCULATOR =====")

try:
    subjects = int(input("Enter number of subjects: "))

    if subjects <= 0:
        print("Please enter at least one subject.")

    else:
        total_points = 0
        total_credits = 0

        for i in range(1, subjects + 1):
            print(f"\nSubject {i}")

            name = input("Enter subject name: ")
            grade = float(input("Enter grade point (0-10): "))
            credit = float(input("Enter credit: "))

            if not (0 <= grade <= 10) or credit <= 0:
                print("Invalid grade or credit.")
                break

            total_points += grade * credit
            total_credits += credit

        else:
            sgpa = total_points / total_credits

            print("\n===== RESULT =====")
            print("Total Credits:", total_credits)
            print(f"SGPA: {sgpa:.2f}")

            if sgpa >= 9:
                print("Performance: Excellent")
            elif sgpa >= 8:
                print("Performance: Very Good")
            elif sgpa >= 7:
                print("Performance: Good")
            elif sgpa >= 6:
                print("Performance: Average")
            else:
                print("Performance: Needs Improvement")

except ValueError:
    print("Please enter valid numeric values.")
