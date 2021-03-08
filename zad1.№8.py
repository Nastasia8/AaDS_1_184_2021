number = int(input("Введите целое шестизначное число: "))
def funct(number):
    i = 1
    while (number!=0):
        i=i*(number%10)
        number=number//10
    print("Произведение цифр равно: ", i)
funct(number)