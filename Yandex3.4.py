def pfunc(s):
    lght = len(s)
    Ctr = [0] * lght    
    Ctr[0] = 0
    for i in range (lght - 1):
        j = Ctr[i]
        while (j > 0) and (s[i + 1] != s[j]):
            j = Ctr[j - 1]
        if (s[i + 1] == s[j]):
            Ctr[i+1] = j + 1
        else:
            Ctr[i + 1] = 0
    return Ctr
txt = str(input())
str = list(txt)

lght = len(str)
pref = pfunc(str)
print(lght - pref[-1])