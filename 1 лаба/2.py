from math import *
def funct (s,g=9.8):
    if s>0:
        t=2*pi*sqrt(s/g)
        print(t)
    else:
        print("Длина не может быть меньше 0, попробуйте еще раз")
s=int(input("Введите длину нити маятника:"))
funct(s)