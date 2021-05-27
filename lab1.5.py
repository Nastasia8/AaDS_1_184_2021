  
def funct(k):
    if k>1:
        p=1
        for n in range(1, k+1):
            p=p*((n+(3**n))/(n+(5**(2*n))))
        print("Прозведение числового ряда равно:", p)
    else:
        print("k должно быть больше 1, попробуйте еще раз")
k=int(input("Введите число:"))
funct(k)