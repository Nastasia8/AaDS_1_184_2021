a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def diag(list):
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if i == j:
                print(a[i][j]*3, end = " ")
            else:
                print(a[i][j], end = " ")
        print()
diag(a)
