a = [6, 2, 9, 13, 1, 8, 4, -5, -11, -8, -2, -6]
s = 0
for i in a[::-1]:
    if i>0:
        break
    s=s+i
print(s)
s1 = 0
i=-1
while a[i] < 0:
    s1+=a[i]
    i-=1
print(s1)
