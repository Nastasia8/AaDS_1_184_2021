def funct (a):
    if a == 0:
        return 0
    if a == 1:
        return 3
    if a ==2:
        return 5
    return funct(a-1)+funct(a-2)+funct(a-3)
for i in range (0,10):
    print(funct(i), end = " ")