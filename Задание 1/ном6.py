# Определить сумму нечетных чисел

def funct(a):
    print("Нечётные числа ---->",[i for i in a if i % 2 == 1])
    s=0
    for i in a:
        if i % 2 == 1:
         s+=i

    print("Сумма нечётных чисел ------>",s)


a = list(range(1,134))
print("Числа ----->",a)
funct(a)
