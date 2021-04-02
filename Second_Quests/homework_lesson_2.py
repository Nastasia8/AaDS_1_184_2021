print('Task_3')
flowers = ['Clematis', 'Dahlia', 'Rose', 'Iris', 'Chrysanthemum', 'Freesia', 'Astilba', 'Lily', 'Peony']
sort_flowers = list(map(lambda x: x[-1], flowers))
print(sort_flowers)
print()

print('Task4')
numbers = list(range(1,26))
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)

print('Task_5')
# Union - объединение
# Intersection - пересечение
A =  {"tiger", 0, "leopard", "elephant", 2, 7}
B = {1, "camel", "elephant", 2, 9}
print()

print(A.union(B))
print(A.intersection(B))

print('Task_6')

# Написать функцию, принимающую два параметра: 1-ый параметр -> множество, 2-ой -> список и возвращающую значение False,
# если хотя бы один из элементов списка не содержится в множестве, иначе возвращающая True
mnoz = {1, 2, 3}
def Function(a, b):
    if (a.intersection(b)):
        print('True')
        return True
    return False



Function(mnoz,numbers)



print('Task_7')
A = (5, 1, 3, 5, 3, 1, 0, 9, 5, 3, 8, 6, 5, 7)
B = [x for x in range(len(A)) if A[x]==5]
print(B)
print()

print('Task_8')
list_= {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6}

def summ(arr):
    result = 0
    for i in arr.values():
        result+=i
    return result

def multiply(arr):
    result= 1
    for i in arr.values():
        result*=i
    return result

print("Summ:", summ(list_))
print("Multiply:", multiply(list_))
print()

print('Task_9')
A = ['Tom', 23, 170, 65, 'Anna', 18, 160, 55, 'Alex', 24, 175, 70, 'Kim', 33, 180, 57]
dict = {}
value = ""

for w in A:
    if type(w) == str:
        dict[w] = []
        string = w
    else:
        dict[string].append(w)
print(dict)

# 10 делается через get, split ', пробел'
d2 ={}
count = 0
text = "Smile, word, Thank, you, smart, Word, smile, Dog, Cat, word, you, cat, he, thank, You, She, hello, she, smile, thanks, dog, Hello, You, and, He, word".lower().split(' , ')
print({word: text.count(word) for word in text})
