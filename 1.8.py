num = int(input("Введите целое: "))
mult = 1
while (num != 0):
    mult = mult * (num % 10)
    num = num // 10
print("Произведение цифр равно: ", mult)