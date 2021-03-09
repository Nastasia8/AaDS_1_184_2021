num =  [6, 2, 9, 13, 1, 8, 4, -5, -11, -8, -2, -6]
x = 0 
for i in num [::-1]:
    if i > 0:
        break
    x = x+i
print (x)


num = [6, 2, 9, 13, 1, 8, 4, -5, -11, -8, -2, -6]
x = 0 
i = -1
while num[i] < 0:
    x+=num[i]
    i-=1
print(x)

