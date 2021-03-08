a = int(input("Введите x: "))
b = int(input("Введите y: "))

while a != 0 and b != 0:

    if a > b:
        a = a % b
    else:
        b = b % a
n = a + b
print("Наибольший общий делитель х и у: ", n)