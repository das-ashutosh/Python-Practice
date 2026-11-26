def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(source, "->", destination)
        return

    hanoi(n - 1, source, destination, auxiliary)

    print(source, "->", destination)

    hanoi(n - 1, auxiliary, source, destination)


disks = int(input("Enter number of disks: "))

if disks <= 0:
    print("Enter a positive number")
else:
    print("Steps to solve Tower of Hanoi:")
    hanoi(disks, "A", "B", "C")
