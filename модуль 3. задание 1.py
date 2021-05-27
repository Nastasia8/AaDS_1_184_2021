def get_hash(s, n, p, x):
    res = 0
    for i in range(n):
        res = (res * x + ord(s[i]))%p
    return res


def rabin_karp(s, t, p, x):
    ht = get_hash(t, len(t), p, x)
    hs = get_hash(s, len(t), p, x)
    xt = 1
    spis = []
    for i in range(len(t)):
        xt = (xt * x) % p
    for i in range((len(s) - len(t)) + 1):
        if ht == hs:
        spis.append(i)
    if i + len(t) < len(s):
       hs = (hs * x -ord(s[i]) * xt + ord(s[i + len(t)]) ) % p

    return spis

def main():
    s = input()
    t = input()
    p = 10**9 + 7
    x = 26
    print(rabin_karp(s, t, p, x))

main()