a=int(input()) 
n=0 
t=list(map(int,input().split(maxsplit=a))) 
for j in range(a-1):
    for i in range(a-j-1):
        if t[i] > t[i + 1]:
            t[i], t[i + 1] = t[i + 1], t[i]
            print(*t, sep=" ")
            n=1
if n == 0:
    print(0)
