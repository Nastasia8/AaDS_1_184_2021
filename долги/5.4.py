def build(v,l,r,segment_tree,nums):
    if r - l == 1:
        segment_tree[v]= nums[l]
        return
    m=(r+l)//2
    build(2*v+1,l,m,segment_tree,nums)
    build(2*v+2,m,r,segment_tree,nums)
    segment_tree[v] = (segment_tree[2*v+1]+segment_tree[2*v+2])
 
def getSum(v,l,r,segment_tree,ql,qr): #эта штучка находит сумму
    if ql<=l and qr>=r:
        return segment_tree[v]
    if ql >= r or qr<=l:
        return 0
    m = (r+l)//2
    st_l = getSum (2*v+1,l,m,segment_tree,ql,qr)
    st_r = getSum (2*v+2,m,r,segment_tree,ql,qr)
    return st_l + st_r
 
def findK(v, l, r, segment_tree, k): #эта штучка находит нули
    if k > segment_tree[v]:
        return -1
    if r - l == 1:
        return r
    m = (r+l)//2
    if segment_tree[2*v+1] >= k:
        return findK(2*v+1, l, m, segment_tree, k)
    else:
        return findK(2*v+2, m, r, segment_tree, k - segment_tree[2*v+1])
 
def main():
    n=int(input())
    numbers= [1 if int(i)==0 else 0 for i in input().split()]
    segment_tree = [0]*4*n
    build(0,0,n,segment_tree,numbers)
    q = int(input())
    arr = []
    while q !=0:
        l,r,k = map(int, input().split())
        sum = getSum(0, 0, n, segment_tree, l-1, r)
        if sum >= k and l == 1:
            arr.append(findK(0, 0, n, segment_tree, k))
        elif sum >= k and l > 1:
            arr.append(findK(0, 0, n, segment_tree, k +(getSum(0, 0, n, segment_tree, 0, l-1))))
        else:
            arr.append(-1)
        q-=1
    print(*arr)
 
 
main()