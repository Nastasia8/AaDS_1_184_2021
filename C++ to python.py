import sys
n=0
p=0
x=0
s=" "
t=" "
def get_hash(i,s,p,x,n):
    res=0
    while int(i)<n:
        res=(res*x+s[i])
        i+=1
    return res

def rabin_karp(i,s,t,p,x,n):
    ht=get_hash(t,sys.getsizeof(t),p,x,n)
    hs=get_hash(s,sys.getsizeof(t),p,x,n)
    xt=1
    while i<sys.getsizeof(t):
        xt=xt*x
        i+=1
        
    while i<=(sys.getsizeof(s)-sys.getsizeof(t)):
        if hs==ht:
            return i
        if (i+sys.getsizeof(t))<sys.getsizeof(s):
            hs=((hs*x)-(s[i]*xt+s[i+sys.getsizeof(t)]))
            hs=(hs+p)
    i+=1
    return -1
s=input()
t=input()
i=0
p=1e9+7
x=26
print(rabin_karp(i,s,t,p,x,n))
