def funct(Matrix):
    for i in Matrix:
        for j in range(len(i)//2):
            i[j], i[-j-1]=i[-j-1], i[j]
    return Matrix
Matrix = [[13,97,56], [17,23,85], [22,45,66]]
print(funct(Matrix))
