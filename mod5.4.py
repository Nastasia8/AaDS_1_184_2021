def build(v,l,r,segment_tree,nums):
    if r - l == 1:
        segment_tree[v]= nums[l]
        return
    m=(r+l)//2
    build(2*v+1,l,m,segment_tree,nums)
    build(2*v+2,m,r,segment_tree,nums)
    segment_tree[v] = (segment_tree[2*v+1]+segment_tree[2*v+2])

def get_sum(v,l,r,segment_tree,ql,qr):
    if ql<=l and qr>=r:
        return segment_tree[v]
    if ql >= r or qr<=l:
        return 0
    m = (r+l)//2
    st_l = get_sum (2*v+1,l,m,segment_tree,ql,qr)
    st_r = get_sum (2*v+2,m,r,segment_tree,ql,qr)
    return st_l + st_r

def find_k(v, l, r, segment_tree, k):
    if k > segment_tree[v]:
        return -1
    if r - l == 1:
        return r
    m = (r+l)//2
    if segment_tree[2*v+1] >= k:
        return find_k(2*v+1, l, m, segment_tree, k)
    else:
        return find_k(2*v+2, m, r, segment_tree, k - segment_tree[2*v+1])

def main():
    n=int(input())
    numbers= [1 if int(i)==0 else 0 for i in input().split()]
    segment_tree = [0]*4*n
    build(0,0,n,segment_tree,numbers)
    q = int(input())
    arr = []
    while q !=0:
        l,r,k = map(int, input().split())
        sum = get_sum(0, 0, n, segment_tree, l-1, r)
        if sum >= k and l == 1:
            arr.append(find_k(0, 0, n, segment_tree, k))
        elif sum >= k and l > 1:
            arr.append(find_k(0, 0, n, segment_tree, k +(get_sum(0, 0, n, segment_tree, 0, l-1))))
        else:
            arr.append(-1)
        q-=1
    print(*arr)


main() 