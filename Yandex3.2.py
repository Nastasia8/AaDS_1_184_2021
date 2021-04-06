def shift(string2, string1, q):

    if string1 == string2: 
        return 0

    string1 += string1

    p = 11
    m = 1
    hash1 = 0
    for i in string2[::-1]:
        hash1 += ord(i) * m
        m *= p
        hash1 %= q
        m %= q

    m = 1
    hash = 0
    for i in string1[:len(string2)][::-1]:
        hash += m * ord(i)
        m *= p
        hash %= q
        m %= q

    hashp = 1
    for i in range(len(string2) - 1):
        hashp *= p
        hashp %= q
    for i in range(1, len(string1) - len(string2) + 1):
        hashn = ((hash % q - ord(string1[i - 1]) * hashp % q) * p % q + ord(string1[i + len(string2) - 1])) % q
        if hashn == hash1:
            return i
        hash = hashn

    return -1

string1 = input()
string2 = input()
q = 2 ** 31 - 1
print(shift(string1, string2, q))
