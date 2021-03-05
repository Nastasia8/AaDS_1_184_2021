#1
def funct(n):
    while n !=1:
        if n %2==0:
           n= n//2
        else:
           n=(n*3)//2
    print(n, end =' ')
n=int(input())
funct(n)

#


