from math import *
def funct (l,g=9.8):
    if l>0:
        a=2*pi*sqrt(l/g)
        print(a)
    else:
        print("невозможно, попробуйте еще раз:")
l=int(input("Введите длину нити маятника:"))
funct(l)
