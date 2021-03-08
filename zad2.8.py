a = {47: 37, 36: 58, 21:4 , 6: 17}
b = 0
c = 1
for i in a:
    b = b + a[i]
for i in a:
    c = c * a[i]
print("Сумма элементов = ", b)
print("Произведение элементов = ", c)