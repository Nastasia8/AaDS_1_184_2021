b=[5, 6, 9, 6, 3, 5, 2, 5, 1]
def funct (s):
    for i in range(len(s)):
        a=s.count(s[i])
        if a > 1:
            s[i] = str(s[i])*a
    return set(s)
print(funct(b))
