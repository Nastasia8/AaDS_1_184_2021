def funct(k):
    n=1
    p=1
    while k >=n:
        p=((n+3**n)/(n+5**(2*n)))*p
        n+=1
    print("Произведение равно =",p)
k = int(input("Введите k = "))
funct(k)  
