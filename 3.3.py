def step ():
    b = []
    y = int(input("Введите 1-ую степень"))
    z = int(input("Введите 2-ую степень"))
    for x in range(1,31):
        if x % 2 != 0:
            x = x**y**z
            b.append(x)
        else:
             b.append(x)
    print(b)
step()