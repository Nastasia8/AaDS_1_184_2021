def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 3
    elif n == 2:
        return 5
    elif n > 0:
        return f(n-1) + f(n-2) + f(n-3)

for i in range(1, 10 + 1):
    print(f(i), end=" ")
print()
