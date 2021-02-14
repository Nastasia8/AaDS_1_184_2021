import math
def calc(x, y, z):
    d = round(math.pow(y, 2) - 4*x*z, 2)
    if d < 0:
        return d
    elif d == 0:
        f = -round(1*y/(2*x))
        return d, f
    else:
        f1 = round((-1*y+math.sqrt(d))/(2*x), 2)
        f2 = round((-1*y-math.sqrt(d))/(2*x), 2)
        return d, f1, f2
x = int(input("X = "))
y = int(input("Y = "))
z = int(input("Z = "))
print(calc(x, y, z))