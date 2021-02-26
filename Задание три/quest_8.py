array = [[2, 5, 4], [3, 1, 9,], [8, 7, 6]]

for i in array:
    for j in i[::-1]:
        print(array[i][j])
    print()
