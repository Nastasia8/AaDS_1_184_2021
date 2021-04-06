a=int(input("Введите первое число последовательности: "))
b=int(input("Введите последнее число последовательности: "))
def funct(a,b):
    summ=0
    for numb in range(a, b):
        if numb%2!=0:
            summ+=numb
    print("Сумма нечётных чисел равна: ", summ)

funct(a,b)