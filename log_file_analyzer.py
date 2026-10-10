from collections import Counter

print("=== Log File Analyzer ===")

filename = input("Enter log file name: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        logs = file.readlines()

    counts = Counter()

    for line in logs:
        for level in ["INFO", "WARNING", "ERROR"]:
            if level in line:
                counts[level] += 1
                break

    print("\n=== Analysis Report ===")
    print("Total log lines:", len(logs))
    print("INFO messages:", counts["INFO"])
    print("WARNING messages:", counts["WARNING"])
    print("ERROR messages:", counts["ERROR"])

except FileNotFoundError:
    print("Log file not found!")

except OSError:
    print("Unable to read the file.")
