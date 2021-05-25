from math import gcd

def build(v, l, r, seg_tree, a):
    if r-l == 1:
        seg_tree[v] = a[l]
        return
    m = (l+r)//2
    build(2*v + 1, l, m, seg_tree, a)
    build(2*v + 2, m, r, seg_tree, a)
    seg_tree[v] = gcd(seg_tree[2*v + 1], seg_tree[2*v + 2])

def get_gcd(v, l, r, seg_tree, ql, qr):
    if ql <= l and qr >= r:
        return seg_tree[v]
    if ql >= r or qr <= l:
        return 0
    m = (r+l)//2
    s_tl = get_gcd(2*v+1, l, m, seg_tree, ql, qr)
    s_tr = get_gcd(2*v+2, m, r, seg_tree, ql, qr)
    return gcd(s_tl, s_tr)

def update(v, l, r, seg_tree, idx, value):
    if r-l == 1:
        seg_tree[v] = value
        return
    m = (r+l)//2
    if idx < m:
        update(2*v+1, l, m, seg_tree, idx, value)
    else:
        update(2*v+2, m, r, seg_tree, idx, value)
    seg_tree[v] = gcd(seg_tree[2*v + 1], seg_tree[2*v + 2])

def main():
    num = int(input())
    seg_tree = [0]*4*num
    a = list(map(int, input().split()))[:num]
    build(0, 0, num, seg_tree, a)
    q = int(input())
    res = []
    while q != 0:
        que, l, r = map(str, input().split())
        if que=="s":
            res.append(get_gcd(0, 0, num, seg_tree, int(l)-1, int(r)))
        else:
            update(0, 0, num, seg_tree, int(l)-1, int(r))
        q -= 1
    print(*res)
main()