# from math import sqrt
# def calc(x,y,z):
#     D = y**2 - 4*x*z
#     if D > 0 and x!= 0:
#         f1 = (-y + sqrt(D))/2*x
#         f2 = (-y - sqrt(D))/2*x
#         print(round(f1,2))
#         print(round(f2,2))
#     elif D == 0 and x!= 0:
#         f1 = (-y)/2*x
#         print(f1)
#     elif D < 0:
#         print("нет решений")
#     else:
#         print("ошибка")
# print("Введите x, y, z")
# calc(int(input()),int(input()),int(input()))

#1
#a = [5, 0, 7, 3, 6, 14, 96, 23, 82, 53]

# через цикл
# nechet = []
# for i in a:
#     if i%2 == 1:
#         nechet.append(i)
# print(nechet)

# list comprehension
# print([i for i in a if i%2==1])

# filter and lambda
# def fun(n):
#     return n % 2 == 1
#print(list(filter(lambda n: n%2==1,a)))

#2
a = list(range(1,26))
#1 способ
# print([i**2 for i in a if i%2==0])
#2 способ
# b = []
# for i in a:
#     if i%2 == 0:
#         b.append(a[i-1]**2)
# print(b)

