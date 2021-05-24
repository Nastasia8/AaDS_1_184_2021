num1 = int(input())
arr1 = [int(i) for i in input().split()][:num1]
num2 = int(input())
arr2 = [int(i) for i in input().split()][:num2]

for i in range(0, num2):
    arr1[arr2[i]-1] -= 1
for i in range(0, num1):
    if (arr1[i] < 0):
        print("yes")
    else:
        print("no")