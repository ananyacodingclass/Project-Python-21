a = int(input("Enter Largest number: "))
b = int(input("Enter Smallest number: "))

if a < b:
    a, b = b, a

lcm = a
while lcm % b != 0:
    lcm += a

print("LCM is :", lcm)