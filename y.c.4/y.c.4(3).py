def menshee(A, n):
    array = [n-1]
    a = [0]*n
    a[n-1] = -1
    for i in range(n-2, -1, -1):
        if A[array[-1]] >= A[i]:
            while (array != []) and (A[array[-1]] >= A[i]):
                array.pop()
            if (array == []):
                a[i] = -1
            else:
                a[i] = array[-1]
            array.append(i)
        else:
            a[i] = array[-1]
            array.append(i)
    return a
            

N = int(input())
A = list(map(int, input().split()))
A = menshee(A, N)
print(' '.join(map(str, A)))