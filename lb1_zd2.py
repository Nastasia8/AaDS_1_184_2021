from math import *
def funct (l,g=9.8):
    if l>0:
        t=2*pi*sqrt(l/g)
        print(t)
    else:
        print("Длина не может быть меньше 0, попробуйте еще раз")
l=int(input("Введите длину нити маятника:"))
funct(l)