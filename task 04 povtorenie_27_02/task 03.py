a = list(int(i) for i in input("enter list: ").split(" "))
b = []
for i in a:
    if i not in b:
        b.append(i)

b.sort()
print(tuple(b))
