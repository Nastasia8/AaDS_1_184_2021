from random import random
M = 10
N = 5
a = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(round(random()*9))
    a.append(b)
    print(b)
print("-------")
e=0
k=1
s=1
for i in range(N):
    b = []
    for j in range(M)[::-1]:
        b.append(round(random() * 9))
        a.append(b)
        print(b)






