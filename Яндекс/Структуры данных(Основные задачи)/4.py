def min_otrezok(A, n, k):
    stack = []
    for i in range(k):
        while (stack != []) and (A[i] <= A[stack[-1]]):
            stack.pop()
        stack.append(i)
    for i in range(k, n):
        print(A[stack[0]])
        while (stack != []) and (i-k >= stack[0]):
            stack.pop(0)
        while (stack != []) and (A[i] <= A[stack[-1]]):
            stack.pop()
        stack.append(i)
    print(A[stack[0]])

N, K = map(int, input().split())
A = list(map(int, input().split()))
min_otrezok(A, N, K) #N-K+1 чисел
#на отрезке K  из N ищет min