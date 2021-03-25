Goods = int(input()) #Вводим кол-во различных товаров
a = list(map(int,input().split(maxsplit=Goods))) #Через пробел вводим количество каждой отдельно взятой категории товаров, не превышая при этом значение "Goods"
Buying = int(input()) #Вводим кол-во заказов клиентов
b = list(map(int,input().split(maxsplit=Buying))) #Через пробел вводим количество заказов в произвольном порядке, не превышая при этом значение "Buying"
for i in range(0, Buying): #Вычитаем кол-во заказов из кол-ва товаров
    a[b[i]-1] -= 1

for i in range(0, Goods): #Проверяем хватает ли у нас на складе товара или нет
    if (a[i] < 0):
        print("yes")
    else:
        print("no")