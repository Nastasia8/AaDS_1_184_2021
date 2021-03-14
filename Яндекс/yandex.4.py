n = int(input())
A = list(int(i) for i in input().split(" "))
print(sum(A[i]>A[j] for i in range(n) for j in range(i+1, n)))
# не проходит по времени, что делать...?