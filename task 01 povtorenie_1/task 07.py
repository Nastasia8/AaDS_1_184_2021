import math

def roots(x, y, z):
    D = y**2 - 4 * x * z
    if D < 0:
        print("No roots")
    elif D == 0:
        print("root =", -y / (2 * x))
    else:
        print("solution 1 = ", (-y + math.sqrt(D))/(2 * x))
        print("solution 2 = ", (-y - math.sqrt(D))/(2 * x))

roots(int(input("Enter x: ")), int(input("Enter y: ")), int(input("Enter z: ")))
