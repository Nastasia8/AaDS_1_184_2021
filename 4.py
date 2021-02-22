import math
def calc(x, y, z):
    return p*math.pow((1+(15/100/(y/12))), y/(12*z))
p = int(input("x ="))
m = int(input("y ="))
n = int(input("z ="))
print(calc(x, y, z))
