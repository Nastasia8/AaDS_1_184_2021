a = {1:12, 2:18, 3:28, 4:32}
b = 1
sum = 0
for i in a:
    sum = sum + a[i]
    b = b*a[i]
print("sum =", sum, "\nb =", b)
