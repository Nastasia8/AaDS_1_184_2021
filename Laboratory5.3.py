a = int(input("Введите a"))
b = int(input("Введите b"))
x = a * b
if a != 0 and b != 0:
    maximum = max(a, b)
    if maximum % a == 0 and maximum % b == 0:
        x = maximum       
    else:
        maximum += 1
        print(x)

