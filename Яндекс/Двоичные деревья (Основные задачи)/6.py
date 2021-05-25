def build(v, l, r, seg_tree, a):
    if r-l == 1:
        seg_tree[v] = a[l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, seg_tree, a)
    build(2*v+2, m, r, seg_tree, a)
    seg_tree[v] = seg_tree[2*v+1] + seg_tree[2*v+2]

def search_k0(v, l, r, seg_tree, k):
    if k > seg_tree[v]:
        return -1
    if r - l == 1:
        return r
    m = (r+l)//2
    if seg_tree[2*v+1] >= k:
        return search_k0(2*v+1, l, m, seg_tree, k)
    else:
        return search_k0(2*v+2, m, r, seg_tree, k - seg_tree[2*v+1])

def get_sum(v, l, r, seg_tree, ql, qr):
    if ql <= l and qr >= r:
        return seg_tree[v]
    if ql >= r or qr <= l:
        return 0
    m = (r+l)//2
    tl = get_sum(2*v+1, l, m, seg_tree, ql, qr)
    tr = get_sum(2*v+2, m, r, seg_tree, ql, qr)
    return tl + tr

def update(v, l, r, seg_tree, ind_new, value):
    if r-l == 1:
        seg_tree[v] = value
        return
    m = (r+l)//2
    if ind_new < m:
        update(2*v+1, l, m, seg_tree, ind_new, value)
    else:
        update(2*v+2, m, r, seg_tree, ind_new, value)
    seg_tree[v] = seg_tree[2*v+1] + seg_tree[2*v+2]
def main():
    n = int(input())
    a = [0 if int(i) != 0 else 1 for i in input().split()]
    seg_tree = [0]*4*n
    build(0, 0, n, seg_tree, a)
    q = int(input())
    ind = []
    while q != 0:
        i = input().split()
        if len(i) == 4:
            l, r, k = int(i[1]), int(i[2]), int(i[3])
            sum_ = get_sum(0, 0, n, seg_tree, l-1, r)
            if sum_ >= k and l > 1:
                ind.append(search_k0(0, 0, n, seg_tree, k+get_sum(0, 0, n, seg_tree, 0, l-1)))
            elif sum_ >= k and l == 1:
                ind.append(search_k0(0, 0, n, seg_tree, k))
            else:
                ind.append(-1)
        else:
            i, v = int(i[1]), int(i[2])
            if v == 0:
                update(0, 0, n, seg_tree, i-1, 1)
            else:
                update(0, 0, n, seg_tree, i-1, 0)
        q -= 1
    print(*ind)
main()