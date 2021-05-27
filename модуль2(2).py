a = int(input())
A = [0]*a
for i in range(a):
    A[i] = list(map(int, input().split()))
A.sort(key=lambda x: x[0])
A.sort(key=lambda x: x[1],reverse=1)
for i in range(a):
    print(A[i][0], A[i][1])
