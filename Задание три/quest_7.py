def Print_Matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = ' ')
        print()


def Calc_Matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i==j:
                print(matrix[i][j]*3, end = ' ')
            else:
                print(matrix[i][j], end = ' ')
        print()

A = [[1,1,1], [1,1,1], [1,1,1]]

Print_Matrix(A)
print()
Calc_Matrix(A)