a = list(input())
b = list(input())
k = 0 
for i in range(len(a)-1):
    while a != b:
        a.insert(0, a.pop())
        k+=1
if a != b:
    k = -1
print(k)

#TL(((