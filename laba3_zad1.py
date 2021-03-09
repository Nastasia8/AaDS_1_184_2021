a =[6, 2, 9, 13, 1, 8, 4, -5, -11, -8, -2, -6]
#цикл for
sum =0
for i in a[::-1]:
    if i>0:
        break
    sum+=i
print(sum)

#while
sum =0
i=-1
while a[i]<0:
    sum+=a[i]
    i-=1
print(sum)
