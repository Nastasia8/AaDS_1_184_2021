def pref_funct(lst,lgth):
    k = [0] * lgth   
    k[0] = 0
    for i in range (lgth - 1):
        j = k[i]
        while (j > 0) and (lst[i + 1] != lst[j]):
            j = k[j - 1]
        if (lst[i + 1] == lst[j]):
            k[i+1] = j + 1
        else:
            k[i + 1] = 0
    return k
N = input()
lgth = len(N)
pref = pref_funct(N,lgth)
print(lgth - pref[-1])