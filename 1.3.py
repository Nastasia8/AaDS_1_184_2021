from math import *


def funct (a, b, s):
    if s =="+":
        print ( "sum =",a+b)
    elif s =="-":
        print("diff =",a-b)
    elif s =="*":
        print("composition =",a*b)
    elif s =="-":
        print("division =",a/b)
    elif s =="**":
        print(" power =",a**2)
        
a = int(input("input a="))
b = int(input("input b="))
s = ("input s=")
funct(a, b, s)