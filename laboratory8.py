
def funct(a):
    p=1
    for i in range (1,7):
        p=p*(a%10)
        a=a//10
    print("Произведение цифр числа равно:",p)

a=int(input("Введите число:"))
if a>=100000:
    funct(a)
else:
    print("Это не шестизначное число, попробуйте еще раз")