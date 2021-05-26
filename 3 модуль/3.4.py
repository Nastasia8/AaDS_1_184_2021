def pref_funct(a,w):
    k = [0] * w    
    k[0] = 0
    for i in range (w - 1):
        j = k[i]
        while (j > 0) and (a[i + 1] != a[j]):
            j = k[j - 1]
        if (a[i + 1] == a[j]):
            k[i+1] = j + 1
        else:
            k[i + 1] = 0
    return k

A = input()
w = len(A)
pref = pref_funct(A,w)
print(w - pref[-1])