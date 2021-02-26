#5
def nok(a,b):
    e = a*b
    while a != 0 and b != 0:
            if a > b:
             a %= b
            else:
             b %= a
    return e//(a+b)

a= int(input("a="))
b = int(input("b="))
print("НОК(",a,";",b,")=",nok(a,b))

# Создать функцию, определяющую наименьшее общее кратное (НОК) двух чисел.
# НОК (a; b) = a*b: НОД (a; b)