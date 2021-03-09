def natasha(num):
    while num != 1:
        if num % 2==0:
            num = num//2
        else:
            num = (num*3+1)//2
        print(num,end='')
a=int(input())
natasha(a)