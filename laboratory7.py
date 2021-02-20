from math import *
def funct (x,y,z):
    if x>0:
        d=y**2-4*x*z
        if d<0:
            print("Корней нет")
        elif d==0:
            f1=(-1*y)/(2*x)
            print("Корень уравнения равен:",f1)
        else:
            f1=(-1*y+sqrt(d))/(2*x)
            f2=(-1*y-sqrt(d))/(2*x)
            print("Первый корень уравнения равен",f1, "\nВторой корень уравнения равен:", f2)
    else:
        print("Уравнение не является квадратным, попробуйте еще раз")
x=int(input("Введите x: "))
y=int(input("Введите y: "))
z=int(input("Введите z: "))
funct(x,y,z)
