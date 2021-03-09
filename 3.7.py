def matrix(x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            print(x[i][j], end = ' ')
        print()
def glavdiagonal(x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            if i==j:
                print(x[i][j]*3, end = ' ')
            else:
                print(x[i][j], end = ' ')
        print()
M=[[1,2,3],[4,5,6],[7,8,9]]
matrix(M)
print("''''''''''''''")
glavdiagonal(M)