#Zadanie 1

a = [5, 0, 7, 3, 6, 14, 96, 23, 82, 53]

#1
nechet = []
for i in a:
    if i%2 != 0:
        nechet.append(i)

print(nechet)

#2
print([i for i in a if i %2 != 0])

#3
def func(n):
    return n % 2 == 1

print(list(filter(func, a)))

#4
print(list(filter(lambda i : i%2 == 1, a)))
