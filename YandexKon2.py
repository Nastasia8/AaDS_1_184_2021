k=0
a=0
i=0
a = int(input())
t = []
for i in range (a):
    t.append(list(map(int,input().split())))
if t[i]==t[i-1]:
    t.sort(key=lambda x:x[0],reverse=False)
else:
    t.sort(key=lambda x:x[1],reverse=True)
for i in t:
    print(*i, sep=' ')
