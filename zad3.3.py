print ( 'Введите x: ')
y = int(input())
print ( 'Введите y: ')
z = int(input())
def kvadr():
    c = []
    for x in range(1,31):
        if x % 2 != 0:
            x = x**y**z
        c.append(x)
    print(c)
kvadr()
    