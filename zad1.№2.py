from math import *
def funct (l,g=9.8):
    if l>0:
        T=2*pi*sqrt(l/g)
        print(T)
    else:
        print("Длина не может быть меньше 0.")
l=int(input("Введите длину нити:"))
funct(l) 