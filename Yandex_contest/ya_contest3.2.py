x = 26
p = 10 ** 9 + 7
def get_hash(a, p, x):
    hash = 0
    for i in range(len(a)):
        hash = (hash * x + ord(a[i])) % p
    return hash

def rehash(a, b, p, x):
    if a == b:
        return 0
    else:
        ha = get_hash(a, p, x)
        hb = get_hash(b, p, x)
        xt = 1
        for i in range(len(a) - 1):
            xt = (xt * x) % p
        for i in range(len(a)):
            if ha == hb:
                return i
            else:
                hb = (x * (hb - ord(b[i]) * xt) + ord(b[i])) % p
        if ha != hb:
            return -1
a = input()
b = input()
print(rehash(a, b, p, x))

