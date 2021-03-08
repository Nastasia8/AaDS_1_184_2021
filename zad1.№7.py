from math import*
x = int(input("Введите переменную x: "))
y = int(input("Введите переменную y: "))
z = int(input("Введите переменную z: "))
def funct(x, y, z):
    D = y**2 - 4*x*z
    if D<0:
        print("Корней нет")
    elif D==0:
        f1=(-1*y/2*x)
        print("Единственный корень = ",f1)
    else:
        f1=(-1*y + sqrt(D))/(2*x)
        f2=(-1*y - sqrt(D))/(2*x)
        print("Пeрвый корень = ",f1)
        print("Второй корень = ",f2)
funct(x, y, z)