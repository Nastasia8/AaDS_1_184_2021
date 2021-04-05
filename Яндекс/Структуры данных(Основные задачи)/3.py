def poisk(A, n):
    stack = [n-1]
    a = [0]*n #a-индексы
    a[n-1] = -1
    for i in range(n-2, -1, -1):
        if A[stack[-1]] >= A[i]:
            while (stack != []) and (A[stack[-1]] >= A[i]):
                stack.pop()
            if (stack == []):
                a[i] = -1
            else:
                a[i] = stack[-1]
            stack.append(i)
        else:
            a[i] = stack[-1]
            stack.append(i)
    return a
            

N = int(input())
A = list(map(int, input().split()))
A = poisk(A, N)
print(' '.join(map(str, A)))