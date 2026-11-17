words = ["listen", "silent", "hello", "below", "elbow", "world"]

checked = []

print("Anagram Pairs:")

for word in words:
    if word not in checked:
        for other in words:
            if word != other and sorted(word) == sorted(other):
                print(word, "-", other)

        checked.append(word)
