def NOD(m,n):
    while m != 0 and n != 0:
        if m > n:
            m %= n
        else:
            n %= m
    return(m+n)
def NOK(m,n):
    return m*n/NOD(m,n)
m=int(input("Введите m: "))
n=int(input("Введите n: "))
print ("НОК (",m, ";",n, ") =", NOK(m,n))
