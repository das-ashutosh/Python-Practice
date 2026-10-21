# Digital Logic Gate Simulator

def logic_gate(gate, a, b):
    if gate == "AND":
        return a and b
    elif gate == "OR":
        return a or b
    elif gate == "XOR":
        return a != b
    elif gate == "NAND":
        return not (a and b)
    elif gate == "NOR":
        return not (a or b)
    elif gate == "XNOR":
        return a == b
    else:
        return None


def display_truth_table(gate):
    print(f"\n===== {gate} GATE TRUTH TABLE =====")
    print("A  B  Output")
    print("----------------")

    for a in [0, 1]:
        for b in [0, 1]:
            result = int(logic_gate(gate, bool(a), bool(b)))
            print(f"{a}  {b}     {result}")


def main():
    gates = ["AND", "OR", "XOR", "NAND", "NOR", "XNOR"]

    print("===== LOGIC GATE SIMULATOR =====")
    print("Available gates:", ", ".join(gates))

    gate = input("Choose a gate: ").strip().upper()

    if gate not in gates:
        print("Invalid gate selected.")
        return

    display_truth_table(gate)

    try:
        a = int(input("\nEnter input A (0 or 1): "))
        b = int(input("Enter input B (0 or 1): "))

        if a not in [0, 1] or b not in [0, 1]:
            print("Inputs must be 0 or 1.")
            return

        output = int(logic_gate(gate, bool(a), bool(b)))
        print(f"\nOutput of {gate}({a}, {b}) = {output}")

    except ValueError:
        print("Please enter valid integer inputs.")


if __name__ == "__main__":
    main()
```
