lst = []
for i in range(4):
    mas = input().split(" ")
    lst.append([])
    for item in mas:
        lst[i].append(int(item))   
for i in range(lst[0][0]):
    n = lst[3].count(i+1)
    for j in range(n):
        lst[1][i] -= 1
    if(lst[1][i] < 0):
        lst[1][i] = "yes"
        print(lst[1][i])
    else:
        lst[1][i]= "no"
        print(lst[1][i])