n = int(input())
arr = []
for i in range(0, n):
    s = list(map(int,input().split()))
    arr.append(s)
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j][1]<arr[j+1][1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        if arr[j][1] == arr[j+1][1]:
            if arr[j][0]>arr[j+1][0]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
for i in arr:
    print(i[0], i[1]) 