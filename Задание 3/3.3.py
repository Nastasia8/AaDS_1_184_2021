#3
print("Последовательность чисел x:")
list_1=list(range(0,30))
b=[]
c=[]
print(list_1)
def stepen(y,z):
    for i in list_1:
        if i%2==1:
            i= i**(y**z)
            b.append(i)
        else:
            b.append(i)
    return b

y=int(input("Введите y="))
z=int(input("Введите z="))
stepen(y,z)
print("С помощью функции:",b)
print("C помощью list comperhention",[i**(y**z) if i%2==1 else i for i in list_1])

# Написать функцию, возводящую нечетные числа из заданной последовательности (от 1 до 30 включительно) в степень,
# например,x^y^z , где - x - число из последовательности, y, z - степень числа, заданные пользователем.
# Из функции вернуть модифицированный список.


