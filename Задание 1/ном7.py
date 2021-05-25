from math import *


def funct (x,y,z):
    d= y * y - 4 * x *z
    print("D=",d)
    if d < 0:
          print("корней нет")
    if d == 0:
          print("один корень")
          f = -y / (2 *x)
          print (f)
    if d > 0:
          print("два корня")
          f =(-y + sqrt(d))/(2 * x)
          f1 =(-y - sqrt(d))/(2 * x)
          print(f)
          print(f1)


x=int(input("input x="))
y=int(input("input y="))
z=int(input("input z="))
funct(x, y, z)