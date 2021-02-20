from math import *
def fun (x,y,num):
    if num==1:
        print(x+y)
    if num==2:
        print(x-y)
    if num==3:
        print(x*y)
    if num==4:
        print(x/y)
x=int(input("input x"))
y=int(input("input y"))
num=int(input("input num"))
fun(x,y,num)