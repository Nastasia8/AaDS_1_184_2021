from math import *
def func(x,y,a): 
    if a==1:
        print(x+y)
    if a==2:
        print(x*y)
    if a==3 and y!=0:
        print(x/y)
    else:
        print("y не может быть равен нулю, попробуйте еще раз")
    if a==4:
        print(x-y)
    if a==5:
        print(x**y)
x=int(input("Введите x: "))
y=int(input("Введите y: "))
a=int(input("Введите a: "))
func(x,y,a)
