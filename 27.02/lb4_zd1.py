def funct(a):
    l=[]
    l.append(a)
    while a!=1:
        if a%2==0:
            a=a//2
            l.append(a)
        else:
            a=(a*3+1)//2
            l.append(a)
        #print(a, end = ' ')
    #print()
    print(l)
n=int(input())
funct(n)
