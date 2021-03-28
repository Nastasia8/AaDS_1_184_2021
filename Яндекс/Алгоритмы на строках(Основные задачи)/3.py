def pref_funct(s):
    n = len(s)
    k = [0] * n    
    k[0] = 0
    for i in range (n - 1):
        j = k[i]
        while (j > 0) and (s[i + 1] != s[j]):
            j = k[j - 1]
        if (s[i + 1] == s[j]):
            k[i+1] = j + 1
        else:
            k[i + 1] = 0
    return k
#префикс функция

text = str(input())
s = list(text)
pref = pref_funct(s)
n=len(s)
for i in range(n - 1, n):
    res = n - pref[i]

if (n % res == 0):
    print(n // res)
else:
    print('1')