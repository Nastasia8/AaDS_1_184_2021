from math import gcd

def build(v, l, r, segment_tree, a): #создаем функцию с переменным
    if r-l == 1:
        segment_tree[v] = a[l]
        return
    m = (l+r)//2
    build(2*v + 1, l, m, segment_tree, a)
    build(2*v + 2, m, r, segment_tree, a)
    segment_tree[v] = gcd(segment_tree[2*v+1], segment_tree[2*v+2])    

def calc(v, l, r, segment_tree, ql, qr): #ф-ия счета НОД на динамических подотрезках
    if ql <= l and qr >= r:
        return segment_tree[v]
    if ql >= r or qr <= l:
        return 0
    m = (l+r)//2
    tl = calc(2*v + 1, l, m, segment_tree, ql, qr)
    tr = calc(2*v + 2, m, r, segment_tree, ql, qr)
    return gcd(tl, tr) 

def update(v, l, r, segment_tree, index, value):
    if r - l == 1:
        segment_tree[v] = value
        return
    middle = (r+l)//2
    if index < middle: #если index < середины то большее возращается
        update(v*2+1, l, middle, segment_tree, index, value)
    else:
        update(v*2+2, middle, r, segment_tree, index, value)
    segment_tree[v] = gcd(segment_tree[2*v+1], segment_tree[2*v+2]) 

def main():  
    n = int(input())
    segment_tree = [0]*(4*n)
    a = list(map(int, input().split()))[:n]
    build(0, 0, n, segment_tree, a)
    q = int(input())
    res = []
    while q != 0:
        t_q, l, r = map(str, input().split())
        if t_q == "s":
            res.append(calc(0, 0, n, segment_tree, int(l)-1, int(r)))
        else:
            update(0, 0, n, segment_tree, int(l)-1, int(r))
        q -= 1
    print(*res)

main()