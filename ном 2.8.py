#8
list_1= {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6}

def s(a):
    result = 0
    for i in a.values():
        result+=i
    return result

def m(a):
    result= 1
    for i in a.values():
        result*=i
    return result
print(list_1)
print("Сумма --->", s(list_1))
print("Перемножение --->", m(list_1))

# Необходимо определить сумму элементов словаря и произведение его элементов