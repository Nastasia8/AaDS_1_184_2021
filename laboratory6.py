def funct(a,b):
    s=0
    for i in range(a,b+1):
        if i%2==1:
            s=s+i
    print("Сумма нечетных чисел в диапазоне равна:", s)
a=int(input("Введите начальное число диапазона: "))
b=int(input("Введите конечное число диапазона: "))
funct(a,b)
