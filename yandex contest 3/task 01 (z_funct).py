def z_funct(s):
    z = [0]*len(s)
    l = r = 0
    for i in range(1, len(s)):
        if i <= r:
            z[i] = min(z[i-l], r - i + 1)
        while z[i] + i < len(s) and s[z[i]] == s[z[i] + i]:
            z[i] += 1
        if z[i] + i - 1 > r:
            l = i
            r = z[i] + i - 1
        
    return z

s = "abcabc"
t = "abc"
z = z_funct(t + '#' + s)

for i in range(len(z)):
    if len(t) == z[i]:
        print(i - len(t) - 1 , end = " ")
