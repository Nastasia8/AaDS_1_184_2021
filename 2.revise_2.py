# Повторение 2
# Задачи 1 и 2 в файле "12 february"

#TASK 3
# words = ["Clematis", "Dahlia", "Rose", "Iris", "Chrysanthemum", "Freesia", "Astilba", "Lily", "Peony"]
# new_start = words.pop()
# new_end = words.pop(0)
# words.append(new_end)
# words.insert(0,new_start)
# print(words)

#TASK 4
# num = list(range(1,26))
# def funny(w):
#     num[0], num[-1] = num[-1], num[0]
#     return num
# print(funny(words))

#TASK 5
# A = {"tiger", 0, "leopard", "elephant",2,7}
# B = {1, "camel", "elephant", 2, 9}
# print(A & B)
# print(A or B)

#TASK 6 делал у доски

#TASK 7
# numbers = (5, 1, 3, 5, 3, 1, 0, 9, 5, 3, 8, 6, 5, 7)
# index = []
# i=0
# for num in numbers:
#     if num == 5:
#         index.append(i)
#     i = i + 1
# print(index)

#TASK 8
# a = {0:1, 1: 5, 2: 60, 3: 3}
# add = 0
# mult = 1
# for i in a:
#     add = add + a[i]
# for i in a:
#     mult = mult * a[i]
# print(a)
# print("Сумма = ", add)
# print("Произведение = ", mult)

#TASK 9
# A = ['Tom', 23, 170, 65, 'Anna', 18, 160, 55, 'Alex', 24, 175, 70, 'Kim', 33, 180, 57]
# dict = {}
# for i in A:
#     if isinstance(i, str):
#         dict[i] = []
#         string = i
#     else:
#         dict[string].append(i)
# print(dict)

#TASK 10
# d ={}
# count = 0
# text = "Smile, word, Thank, you, smart, Word, smile, Dog, Cat, word, you, cat, he, thank, You, She, hello, she, smile, thanks, dog, Hello, You, and, He, word".lower().split(' , ')
# for word in text:
#     if word in d:
#         count+=1
#     else:
#         d[word]=1
#     d[word] = d.get(word, 0) + 1
# print({word: text.count(word) for word in text})



