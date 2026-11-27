from collections import Counter

logs = [
    "GET /home 200",
    "GET /about 200",
    "POST /login 401",
    "GET /dashboard 200",
    "GET /profile 404",
    "POST /data 500",
    "GET /home 200"
]

status_codes = []

for line in logs:
    parts = line.split()
    status_codes.append(parts[-1])

counts = Counter(status_codes)

print("HTTP Status Report:")

for code, count in sorted(counts.items()):
    print(code, ":", count)

print("Total Requests:", len(logs))
print("Failed Requests:", sum(
    count for code, count in counts.items()
    if code.startswith(("4", "5"))
))
