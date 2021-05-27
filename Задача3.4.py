def z_funct(s):
    p = [0]*len(s)
    for i in range(len(s)-1):
        j = p[i]
        while j>0 and s[i+1]!=s[j]:
            j = p[j-1]
        if s[i+1]==s[j]:
            p[i+1]=j+1
        else:
            p[i+1]=0
    return p
s = input()
z = z_funct(s)
print(len(s)-z[-1])
    