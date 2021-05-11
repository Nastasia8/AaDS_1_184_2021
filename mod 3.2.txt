def shift(a, b, c):

    if b == a: 
        return 0

    b += b

    p = 11
    m = 1
    hash1 = 0
    for i in a[::-1]:
        hash1 += ord(i) * m
        m *= p
        hash1 %= c
        m %= c

    m = 1
    hash = 0
    for i in b[:len(a)][::-1]:
        hash += m * ord(i)
        m *= p
        hash %= c
        m %= c

    hashp = 1
    for i in range(len(a) - 1):
        hashp *= p
        hashp %= c
    for i in range(1, len(b) - len(a) + 1):
        hashn = ((hash % c - ord(b[i - 1]) * hashp % c) * p % c + ord(b[i + len(a) - 1])) % c
        if hashn == hash1:
            return i
        hash = hashn

    return -1

b = input()
a = input()
c = 2 ** 31 - 1
print(shift(b, a, c))