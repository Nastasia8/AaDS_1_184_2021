def hash(A, n):
    res = 0
    for i in range(n):
        res = (res * p + ord(A[i])) % d
    return res

def rabin_karp(s, q, n):
    hs_hash = hash(s, n)
    hq_hash = hash(q, n)
    
    dq = 1
    for i in range(n-1):
        dq = (dq * p) % d
    if hs_hash == hq_hash:
        return 0
    for i in range(n-1):
        hq_hash = (hq_hash - ord(q[i]) * dq) * p
        hq_hash += ord(q[i])
        hq_hash %= d       
        if hs_hash== hq_hash:
            return i+1
    return -1 

s = input()
q = input()

p = 31
d = 2 ** 31 - 1

A = rabin_karp(s, q, len(s))
print(A)