# программа считает период математического маятника
from math import *


def funct(l, g):
    t = 2 * pi * sqrt(l / g)
    print(t)


l = int(input("Введите l --->"))
g = int(input("Введите g --->"))
funct(l, g)
