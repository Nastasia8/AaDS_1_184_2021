def prefix(n):
    pref = [0] * len(n)
    for i in range(len(n) - 1):
        k = pref[i]
        while k > 0 and n[i + 1] != n[k]:
            k = pref[k - 1]
        if n[i + 1] == n[k]:
            pref[i + 1] = k + 1
        else:
            pref[i + 1] = 0
    return pref


a = input()
pr = prefix(a)
res = len(a) - pr[-1]
if len(a) % res == 0:
    print(len(a) // res)
else:
    print('1')