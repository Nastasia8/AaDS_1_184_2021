a = {}
b = ["Tom", 23, 170, 65, "Anna", 18, 160, 55, "Alex", 24, 175, 70, "Kim", 33, 180, 57]
string = " "
for w in b:
    if type(w) == str:
     a[w] = []
     string = w 
    else:
     a[string].append(w)
print(a)