n = int(input())
A = [0]*n
for i in range(n):
    A[i] = list(map(int, input().split()))
A.sort(key=lambda x: x[0])
A.sort(key=lambda x: x[1],reverse=1)
for i in range(n):
    print(A[i][0], A[i][1])