def funct(a):
    if n == 0:
        return 0
    if n == 1:
        return 3
    if n == 2:
        return 5
    return funct(n-1)+f(n-2)+f(n-3)
for i in range(0,10):
    print(funct(i), end= " ")