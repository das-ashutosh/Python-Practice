import time

sentence = "Python is fun to learn and easy to practice"

print("=== Typing Speed Tester ===")
print("\nType this sentence:")
print(sentence)

input("\nPress Enter when you are ready...")
start_time = time.time()

typed_text = input("\nStart typing: ")

end_time = time.time()
elapsed_time = end_time - start_time

words = len(typed_text.split())
speed = (words / elapsed_time) * 60 if elapsed_time > 0 else 0

print("\n=== Your Results ===")
print(f"Time taken: {elapsed_time:.2f} seconds")
print(f"Typing speed: {speed:.2f} words per minute")

if typed_text == sentence:
    print("Accuracy: 100%")
else:
    print("The typed sentence does not match exactly.")
