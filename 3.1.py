list = [6, 2, 9, 13, 1, 8, 4, -5, -11, -8, -2, -6]
sum = 0
for i in list[::-1]:
    if i>0:
        break
    sum=sum+i
print(sum)
sum1 = 0
i=-1
while list[i] < 0:
    sum1+=list[i]
    i-=1
print(sum1)
