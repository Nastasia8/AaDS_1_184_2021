def z_funct(s):
    z=[0]*len(s)
    l=r=0
    for i in range(1,len(s)):
        if i<=r:
            z[i]=min(z[i-l],r-i+1)
        while z[i]+i<len(s) and s[z[i]]==s[z[i]+i]:
            z[i]+=1
        if z[i]+i-1>r:
            l=inputr=z[i]+i-1
    return z

s=input()
print(z_funct(s))