#5
a={'tiger', 0, 'leopard', 'elephant', 2, 7}
b={1, 'camel', 'elephant', 2, 9}
c=[]
for i in a:
    for j in b:
        if i==j :
            c.append(i)

print("Решение 1",c)
print(a.intersection(b))
print("Решение 2")
print(a.union(b))#объединение
print(a.intersection(b))#пересечение

#Дано множество А{“tiger”, 0, “leopard”, “ elephant”,  2, 7} и B{1, “camel”, “elephant”, 2, 9}
# отобразить результат пересечения и объединения множеств
