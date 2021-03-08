a = []
for i in range(1,26):
    if i % 2 == 0:
        i **= 2
        a.append(i)
print("Четныe =", a)
def funct(a):
    a[0], a[-1] = a[-1], a[0]
    return a
print(funct(a))
