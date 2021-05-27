def prefix(a,n):
    k = [0] * len(n)   
    k[0] = 0
    for i in range (len(n) - 1):
        j = k[i]
        while j > 0 and (n[i + 1] != n[j]):
            j = k[j - 1]
        if (n[i + 1] == n[j]):
            k[i+1] = j + 1
        else:
            k[i + 1] = 0
    return k


n = input()
a = len(n)
res = prefix(a,n)
k = a - res[a-1]
if (a % k == 0):
    print(a//k)
else:
    print(1)
    