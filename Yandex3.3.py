
def pref_func(lst):
    lgth = len(lst)
    Ctr = [0] * lgth    
    Ctr[0] = 0
    for i in range (lgth - 1):
        j = Ctr[i]
        while (j > 0) and (lst[i + 1] != lst[j]):
            j = Ctr[j - 1]
        if (lst[i + 1] == lst[j]):
            Ctr[i+1] = j + 1
        else:
            Ctr[i + 1] = 0
    return Ctr

txt = str(input())
lst = list(txt)

lgth = len(lst)
pref = pref_func(lst)

for i in range(lgth - 1, lgth):
    result = lgth - pref[i]

if (lgth % result == 0):
    print(lgth // result)
else:
    print('1')