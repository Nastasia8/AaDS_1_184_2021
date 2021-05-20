def clsdvig(s, t, c):
    if s==t:
        return 0
    else:
        t*=2
        p = 11
        m = 1
        sh = 0
        for i in s[::-1]:
            sh += ord(i) * m
            m *= p
            sh %= c
            m %= c

        m = 1
        hash = 0
        for i in t[:len(s)][::-1]:
            hash += m * ord(i)
            m *= p
            hash %= c
            m %= c

        ht = 1
        for i in range(len(s) - 1):
            ht *= p
            ht %= c
        for i in range(1, len(t) - len(s) + 1):
            hn = ((hash % c - ord(t[i - 1]) * ht % c) * p % c + ord(t[i + len(s) - 1])) % c
            if hn == sh:
                return i
            hash = hn

        return -1

s = input()
t = input()
c = 2**31 - 1
print(clsdvig(s,t,c))
