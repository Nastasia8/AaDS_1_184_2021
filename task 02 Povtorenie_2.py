########## TASK 1 ##########

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

########## TASK 2 ##########

a = list(range(1, 26))

#1
chet = []

for item in a:
    if item % 2 == 0:
        chet.append(item**2)
    else:
        chet.append(item)

print(chet)

#2
print(list(chet**2 if chet % 2 == 0 else chet for chet in a))

########## TASK 3 ##########

a = ["Clematis", "Dahlia", "Rose", "Iris", "Chrysanthemum", "Freesia", "Astilba", "Lily", "Peony"]

#1
w = []
for word in a:
    w.append(word[-1])
    
print(w)

#2
print(list([word[-1] for word in a]))

#3
print(list(map(lambda word : word[-1], a)))

########## TASK 4 ##########

a = list(range(1, 26))

a[-1], a[0] = a[0], a[-1]
print(a)

########## TASK 5 ##########

a = {"tiger", 0, "leopard", "elephant",  2, 7}
b = {1, "camel", "elephant", 2, 9}

#1
c = []

for i in a:
    for j in b:
        if i == j:
            c.append(i)

print(c)

#2
print(a.intersection(b))

########## TASK 6 ##########

mn = {"tiger", 0, "leopard", "elephant", 2, 7}
list = list(range(1, 26))

def sameEl(list, el):
    return (True if mn.intersection(list) != set() else False)
    
print(sameEl(list, mn))

########## TASK 7 ##########

a = (5, 1, 3, 5, 3, 1, 0, 9, 5, 3, 8, 6, 5, 7)
value5 = []

for i in range(0, len(a)):
    if a[i] == 5:
        value5.append(i)
        
print(value5)

########## TASK 8 ##########

a = (5, 1, 3, 5, 3, 1, 9, 5, 3, 8, 6, 5, 7)
sum = 0
mlt = 1

for i in a:
    sum += i
    mlt *= i

print(sum)
print(mlt)

########## TASK 9 ##########

a = ["Tom", 23, 170, 65, "Anna", 18, 160, 55, "Alex", 24, 175, 70, "Kim", 33, 180, 57]
d = {}

value = ""

for i in a:
    if type(i) == str:
        value = i
        d[value] = []
    else:
        d[value].append(i)
        
print(d)

########## TASK 10 #########

text = "Smile, word, Thank, you, smart, Word, smile, Dog, Cat, word, you, cat, he, thank, You, She, hello, she, smile, thanks, dog, Hello, You, and, He, word"

a = text.lower().split(", ")
d1 = {}

#1
for word in a:
    if word in d1:
        d1[word] += 1
    else:
        d1[word] = 1

print(d1)

#2
d2 = {}
for word in a:
    d2[word] = d2.get(word, 0) + 1
print(d2)

##3
print({word: text.count(word) for word in a})
