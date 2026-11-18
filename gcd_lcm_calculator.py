import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = math.gcd(a, b)

if a == 0 and b == 0:
    lcm = 0
else:
    lcm = abs(a * b) // gcd

print("GCD:", gcd)
print("LCM:", lcm)
