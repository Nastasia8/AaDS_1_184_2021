def prefix(A):
    pref = [0] * len(A)
    for i in range(len(A) - 1):
        j = pref[i]
        while j > 0 and A[i + 1] != A[j]:
            j = pref[j - 1]
        if A[i + 1] == A[j]:
            pref[i + 1] = j + 1
        else:
            pref[i + 1] = 0
    return pref


a = input()
pr = prefix(a)
res = len(a) - pr[-1]
if len(a) % res == 0:
    print(len(a) // res)
else:
    print(1)