# счёт простых математических операций
from math import *


def funct(x, y, op):
    if op =="+":
        print("Функция сложения = х + у =",x+y)
    elif op =="-":
        print("Функция вычитания = х - у =",x-y)
    elif op =="*":
        print("Функция умножения = х * у =",x*y)
    elif op =="/":
        print("Функция деления = х / у =",x/y)
    elif op =="**":
        print("Функция возведения в степень = х ^ у =",x**y)


x= int(input("Введите x --->"))
y= int(input("Введите y --->"))
op= input("Введите операцию --->")
funct(x, y, op)
