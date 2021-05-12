def poezd(A, N):
    a = []
    B = []
    pd_sort = sorted(A)
    while len(B) != N:
        if not a:
            a.append(A[0])
            A.pop(0)
        if (len(A) > 0) and (A[0] <= a[-1]):
            a.append(A[0])
            A.pop(0)
        else:
            B.append(a[-1])
            a.pop()
    return B == pd_sort


N = int(input())
inA = list(map(int, input().split()))
if poezd(inA, N):
    print("YES")
else:
    print("NO")
