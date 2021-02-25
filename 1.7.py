from math import *


def funct (x, y, d):
    d = y ** 2 - 4 * x *2
    print("d=", d)
    if d == 0:
        print("one root")
        f = - y / (2*x)
        print(f)
    elif d < 0:
        print("no root")
    elif d > 0:
        print("two roots")
        f1 = (- y + sqrt(d))/ (2*x)
        f2 = (- y - sqrt(d))/ (2*x)
        print(f1)
        print(f2)
        
        
x = int(input("input x="))
y = int(input("input y="))
d = ("input d=")
funct(x, y, d)
