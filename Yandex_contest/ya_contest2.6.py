size_1 = int(input())
arr_1 = [int(i) for i in input().split()][:size_1]
size_2 = int(input())
arr_2 = [int(i) for i in input().split()][:size_2]

for i in range(0, size_2):
    arr_1[arr_2[i]-1] -= 1
for i in range(0, size_1):
    if (arr_1[i] < 0):
        print("yes")
    else:
        print("no")