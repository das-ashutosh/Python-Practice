import time

print("Stopwatch started!")
start = time.time()
input("Press Enter to stop...")
end = time.time()
elapsed = end - start
print("Time elapsed:", round(elapsed, 2), "seconds")
