a = [6, 2, 9, 13, 1, 8, 4, -5, -11, -8, -2, -6]

#1

sum = 0
for i in reversed(a):
    if i < 0:
        sum += i
print(sum)

#2

sum = 0
i = -1
while a[i] < 0:
    sum += a[i]
    i -= 1;
print(sum)
