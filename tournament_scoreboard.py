players = {}
print("🏆 Tournament Scoreboard")
for i in range(3):
    name = input("Enter player name: ")
    score = int(input("Enter player score: "))
    players[name] = score

print("\n=== Scoreboard ===")

for name, score in players.items():
    print(name, ":", score)

winner = max(players, key=players.get)

print("\n🏆 Winner:", winner)
print("Score:", players[winner])
