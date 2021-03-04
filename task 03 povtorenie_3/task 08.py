a = [[4, 3, 5, 1], [0, 7, 2, 9], [2, 6, 3, 8]]
b = [[13, 97, 56], [17, 23, 85], [22, 45, 66]]
     
#1

def revMatrix(list):
    for i in range(0, len(list)):
        for j in list[i][::-1]:
            print(" ".join(str(l) for l in [j]), end = " ")
        print()

revMatrix(a)
print()
revMatrix(b)

#2

def cout(list):
    for i in range(0, len(list)):
        print(" ".join(str(j) for j in list[i]))

def revMatrix(list):
    for i in range(0, len(list)):
        revList(list[i])
    cout(list)

def revList(list):
    for i in range(0, int(len(list)/2)):
        list[i], list[len(list) - i - 1] = list[len(list) - i - 1], list[i]

print()
revMatrix(a)
print()
revMatrix(b)
