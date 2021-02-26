def funct(x):
    if x>1:
        p=1
        for n in range(1, x+1):
            p=p*((n+(3**n))/(n+(5**(2*n))))
        print("Прозведение числового ряда равно:", p)
    else:
        print("x должно быть больше 1, попробуйте еще раз")
x=int(input("Введите число:"))
funct(x)