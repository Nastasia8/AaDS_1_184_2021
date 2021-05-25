#1 способ
def choose(n, k):
    if k in (0, n):
        return 1
    return choose(n - 1, k - 1) + choose(n - 1, k)
for row in range(10):
    for k in range(row+1):
        print(choose(row, k), end=' ')
    print()

#2 cпособ

def vizov(h):
    b=[1]
    a=[0]
    for j in range(h):
        print(b)
        b=[left+right for left, right in zip(b+a,a+b)]
    return(b)


h=10
vizov(h)