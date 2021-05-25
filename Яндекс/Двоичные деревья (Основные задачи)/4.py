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
    s_tl = get_sum(2*v+1, l, m, seg_tree, ql, qr)
    s_tr = get_sum(2*v+2, m, r, seg_tree, ql, qr)
    return s_tl + s_tr
def main():
    num = int(input())
    a = [0 if int(i) != 0 else 1 for i in input().split()]
    seg_tree = [0]*4*num
    build(0, 0, num, seg_tree, a)
    q = int(input())
    ind = []
    while q != 0:
        l, r, k = map(int, input().split())
        sum = get_sum(0, 0, num, seg_tree, l-1, r)
        if sum >= k and l > 1:
            ind.append(search_k0(0, 0, num, seg_tree, k+get_sum(0, 0, num, seg_tree, 0, l-1)))
        elif sum >= k and l == 1:
            ind.append(search_k0(0, 0, num, seg_tree, k))
        else:
            ind.append(-1)
        q -= 1
    print(*ind)
main()