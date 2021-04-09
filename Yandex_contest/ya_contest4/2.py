def train(A, n):
    a = []
    B = []
    tr_sort = sorted(A)
    while len(B) != n:
        if not a:
            a.append(A[0])
            A.pop(0)
        if (len(A) > 0) and (A[0] <= a[-1]):
            a.append(A[0])
            A.pop(0)
        else:
            B.append(a[-1])
            a.pop()
    return B == tr_sort


n = int(input())
inA = list(map(int, input().split()))
if train(inA, n):
    print("YES")
else:
    print("NO")