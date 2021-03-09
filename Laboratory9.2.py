a={}
list= ["Tom", 23, 170, 65, "Anna", 18, 160, 50, "Alex", 24, 175, 70, "Kim", 33, 180, 57]
string = ""
for i in list:
    if type(i)==str:
        a[i]=[]
        string=i
    else:
        a[string].append(i)
print(a)
