
size1 = int(input())
a = list(int(i) for i in input().split(" "))[:size1]
size2 = int(input())
b = list(int(i) for i in input().split(" "))[:size2]

for i in range(0, size2):
    a[b[i]-1] -= 1

for i in range(0, size1):
    if (a[i] < 0):
        print("yes")
    else:
        print("no")