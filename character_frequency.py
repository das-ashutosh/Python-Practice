text = input("Enter a sentence: ")

frequency = {}

for char in text.lower():
    if char != " ":
        frequency[char] = frequency.get(char, 0) + 1

print("\n===== CHARACTER FREQUENCY =====")

for char, count in frequency.items():
    print(char, ":", count)
