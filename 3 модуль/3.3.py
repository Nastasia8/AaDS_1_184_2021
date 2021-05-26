#на яндексе ошибка представления, что это?))

def pref_func(a):
    b = len(a)
    c = [0] * b    
    c[0] = 0
    for i in range (b - 1):
        j = c[i]
        while (j > 0) and (a[i + 1] != a[j]):
            j = c[j - 1]
        if (a[i + 1] == a[j]):
            c[i+1] = j + 1
        else:
            c[i + 1] = 0
    return c

txt = str(input())
a = list(txt)

b = len(a)
pref = pref_func(a)

for i in range(b - 1, b):
    result = b - pref[i]

if (b % result == 0):
    print(b // result)
else:
    print('1')