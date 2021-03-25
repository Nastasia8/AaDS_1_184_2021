a = {9: 7, 6: 5, 2:4 , 3: 7}
x = 0
for i in a:
    x = x + a[i]
y = 1
for i in a:
    y = y * a[i]
print("sum = ", x)
print("com = ", y)