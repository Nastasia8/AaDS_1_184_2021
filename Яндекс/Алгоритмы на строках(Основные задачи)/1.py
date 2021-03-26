def get_hash(s, k, p, d):
    res = 0
    for j in range(0, k):
        res=(res*d+ord(s[j]))%p
    return res


def rabin_karp(s, q, p, d):
    hq=get_hash(q, len(q), p, d)
    hs=get_hash(s, len(q), p, d)
    dq=1
    l=[]
    for j in range (len(q)):
        dq=(dq*d)%p
    for j in range(len(s)-len(q)+1):
        if hq==hs:
            l.append(j)
        if j+len(q)<len(s):
            hs=(hs*d-ord(s[j])*dq+ord(s[j+len(q)]))%p

    print(" ".join(map(str, l)))
def main():
    s=input()
    q=input()
    p=1e9+7
    d=26
    rabin_karp(s,q,p,d)
main()