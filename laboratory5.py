def funct(k):
    if k>1:
        proiz=1
        for n in range(1, k+1):
            proiz=proiz*((n+(3**n))/(n+(5**(2*n))))
        print("Прозведение числового ряда равно:", proiz)
    else:
        print("k должно быть больше 1, попробуйте еще раз")
k=int(input("Введите число:"))
funct(k)
