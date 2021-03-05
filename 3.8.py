n = [[9,5,6], [8,4,3], [9,8,1]]
for i in n:
    for j in i[::-1]:
        print(n[i][j])
    print()
