# не проходит по времени :(
n = int(input())
arr = [int(i) for i in input().split()]
ct = 0
for i in range(n-1):
    for j in range(i + 1, n):
        if arr[i] > arr[j]:
            ct += 1
print(ct)


