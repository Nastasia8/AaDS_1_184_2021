k=int(input("Введите число k: "))
def funct(k):
    P=1
    for n in range(1, k+1):
        P=P*((n+3**n)/(n+(5**(2*n))))
        print("Произведение равно: ", P)
funct(k)