import math

def calculate(l, g = 9.8):
    if g != 0:
        return 2 * math.pi * math.sqrt(l * g)
    else:
        print("error")

print("Answer :", calculate(int(input("Enter l value: ")))
