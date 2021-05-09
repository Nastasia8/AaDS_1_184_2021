import math
def build(v, l, r, segm_tree, nums):
    if r-l == 1:
        segm_tree[v] = nums[l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, segm_tree, nums)
    build(2*v+2, m, r, segm_tree, nums)
    segm_tree[v]= math.gcd(segm_tree[2*v+1], segm_tree[2*v+2])
def get(v, l, r, segm_tree, ql, qr):
    if ql <= l and qr >= r:
        return segm_tree[v]
    if ql>=r or qr<=l:
        return 0
    m =(r+l)//2
    st_l=get(2*v+1, l, m, segm_tree, ql, qr)
    st_r = get(2*v+2, m, r, segm_tree, ql, qr)
    return math.gcd(st_l, st_r)
def main():
    n=int(input())
    nums = list(map(int, input().split()))[:n]
    segment_tree = [0]*4*n
    build(0, 0, n, segment_tree, nums)
    q = int(input())
    arr = []
    while q!=0:
        l, r = map(int,input().split())
        arr.append(get(0, 0, n, segment_tree, l-1, r))
        q-=1
    print(*arr)
main()