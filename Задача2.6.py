n = int(input()) #количество видов на складе
c = [int(i) for i in input().split()] # количество товаров вида на складе
k = int(input()) # количество заказов
a = [int(i) for i in input().split()] # заказы клиентов
for i in range(0, k):
    c[(a[i]) - 1] = c[(a[i])-1] - 1
for i in c:
    if i <0:
        print('yes')
    else:
        print('no')
