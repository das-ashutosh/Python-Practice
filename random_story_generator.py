import random

names = ["Rahul", "Amit", "Priya", "Riya"]
places = ["a forest", "a college", "the moon", "a beach"]
animals = ["tiger", "monkey", "elephant", "cat"]
actions = ["dancing", "singing", "running", "cooking"]

name = random.choice(names)
place = random.choice(places)
animal = random.choice(animals)
action = random.choice(actions)

print(" Random Story Generator ")
print()
print(f"One day, {name} went to {place}.")
print(f"Suddenly, a {animal} appeared!")
print(f"The {animal} started {action}.")
print(f"{name} laughed and had an unforgettable day!")
