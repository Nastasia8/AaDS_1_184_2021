a = [5, 0, 7, 3, 6, 14, 96, 23, 82, 53]
def fun(n):
    return n % 2 == 1
print(list(filter(fun,a)))