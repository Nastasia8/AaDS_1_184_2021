a=[5, 0, 7, 3, 6, 14, 96, 23, 82, 53]
b=[]
for num in a:
    if num %2 == 1:
       b.append(num)
for num in b:
   print(num) 
a = [5, 0, 7, 3, 6, 14, 96, 23, 82, 53]
print([i for i in a if i %2 == 1])
a = [5, 0, 7, 3, 6, 14, 96, 23, 82, 53]
def fun(n):
    return n %2 == 1
print(list(filter(fun, a)))
a = [5, 0, 7, 3, 6, 14, 96, 23, 82, 53]
print(list(filter(lambda n: n %2 == 1, a)))
