#3-4 задача 5 модуль
#RMQ - нахождение максимума на отрезке
#RSQ - нахождение сумма на отрезке
#5  8 13 6 24               [0, 5) - > [0, 2) and [2, 5) - >(([0, 2))) -> [0, 1) and [1, 2)
#МОД на подотрезках, поиск максимума
def build(v, l, r, segm_tree, nums):
    if r-l == 1:
        segm_tree[v] = nums[l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, segm_tree, nums)
    build(2*v+2, m, r, segm_tree, nums)
    segm_tree[v]= (segm_tree[2*v+1] + segm_tree[2*v+2])
def get(v, k, segm_tree, l, r, res):
    if k > segm_tree[v]:
        return -1
    if l == r:
       return res
    m = (l+r)//2
    if segm_tree[v*2] >= k:
        return get(v*2, l, m, k, segm_tree, res)
    else:
        return get(v*2+1, m+1, r, k - segm_tree[v*2], segm_tree, res)

def main():
    n=int(input())
    nums = list(map(int, input().split()))[:n]
    segment_tree = [0]*4*n
    build(0, 0, n, segment_tree, nums)
    q = int(input())
    arr = []
    while q!=0:
        l, r, k = map(int,input().split())
        get(l-1, l, r, k, segment_tree, r)
        q-=1
    print(*arr)
main()

#MОД на подотрезках, поиск индекса максимума
def build(v, l, r, segm_tree, nums):
    if r-l == 1:
        segm_tree[v] = [nums[l], l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, segm_tree, nums)
    build(2*v+2, m, r, segm_tree, nums)
    segm_tree[v]= max(segm_tree[2*v+1], segm_tree[2*v+2])
def getMax(v, l, r, segm_tree, ql, qr):
    if ql <= l and qr >= r:
        return segm_tree[v]
    if ql>=r or qr<=l:
        return [-1e9, -1]
    m =(r+l)//2
    st_l=getMax(2*v+1, l, m, segm_tree, ql, qr)
    st_r = getMax(2*v+2, m, r, segm_tree, ql, qr)
    return max(st_l, st_r)
def main():
    n=int(input())
    nums = list(map(int, input().split()))[:n]
    segment_tree = [[0, 0]]*4*n
    build(0, 0, n, segment_tree, nums)
    q = int(input())
    arr = []
    while q!=0:
        l, r, k = map(int,input().split())
        arr.append(getMax(0, 0, n, segment_tree, l-1, r))
        q-=1
    # print(*arr)
    [print(i[1]+1, end =" ") for i in arr]
main()

#количество максимумов на отрезках
def build(v, l, r, segm_tree, nums):
    if r-l == 1:
        segm_tree[v] = [nums[l], 1]
        return
    m = (r+l)//2
    build(2*v+1, l, m, segm_tree, nums)
    build(2*v+2, m, r, segm_tree, nums)
    st_l = segm_tree[2*v+1] #[*, *]
    st_r = segm_tree[2*v+2]
    if st_r[0]>st_l[0]:
        segm_tree[v] = st_r
    elif st_r[0] > st_l[0]:
        segm_tree[v] = st_l
    else:
        segm_tree[v] = [st_r[0], st_l[1]+st_l[1]]
def getMax(v, l, r, segm_tree, ql, qr):
    if ql <= l and qr >= r:
        return segm_tree[v]
    if ql>=r or qr<=l:
        return [-1e9, -1]
    m =(r+l)//2
    st_l=getMax(2*v+1, l, m, segm_tree, ql, qr)
    st_r = getMax(2*v+2, m, r, segm_tree, ql, qr)
    if st_r[0] > st_l[0]:
        return st_r
    elif st_r[0] > st_l[0]:
        return st_l
    else:
        return [st_r[0], st_l[1] + st_l[1]]
def main():
    n=int(input())
    nums = list(map(int, input().split()))[:n]
    segment_tree = [[0, 0]]*4*n
    build(0, 0, n, segment_tree, nums)
    q = int(input())
    arr = []
    while q!=0:
        l, r = map(int,input().split())
        arr.append(getMax(0, 0, n, segment_tree, l-1, r))
        q-=1
    # print(*arr)
    for e, k in arr:
        print(e, k)
main()
