a = ["Tom", 23, 170, 65, "Anna", 18, 160, 55, "Alex", 24, 175, 70, "Kim", 33, 180, 57]
d = {}

value = ""

for i in a:
    if type(i) == str:
        value = i
        d[value] = []
    else:
        d[value].append(i)
        
print(d)
