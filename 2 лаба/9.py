d={}
lista= ["Tom", 23, 170, 65, "Anna", 18, 160, 50, "Alex", 24, 175, 70, "Kim", 33, 180, 57]
string = ""
for w in lista:
    if type(w)==str:
        d[w]=[]
        string=w
    else:
        d[string].append(w)
print(d)