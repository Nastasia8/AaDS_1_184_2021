# #МОД на подотрезках, поиск максимума  1
def build(v, l, r, segm_tree, nums):
    if r-l == 1:
        segm_tree[v] = nums[l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, segm_tree, nums)
    build(2*v+2, m, r, segm_tree, nums)
    segm_tree[v]= max(segm_tree[2*v+1], segm_tree[2*v+2])

def getMax(v, l, r, segm_tree, ql, qr):
    if ql <= l and qr >= r:
        return segm_tree[v]
    if ql>=r or qr<=l:
        return -1e9
    m =(r+l)//2
    st_l=getMax(2*v+1, l, m, segm_tree, ql, qr)
    st_r = getMax(2*v+2, m, r, segm_tree, ql, qr)
    return max(st_l, st_r)

def update(v, l, r, segment_tree, indx, value):
    if r-l == 1:
        segment_tree[v] = value
        return
    m = (l+r)//2
    if indx < m:
        update(2*v+1, l, m, segment_tree, indx, value)
    else:
        update(2*v+2, m, r, segment_tree, indx, value)
    segment_tree[v]=max(segment_tree[2*v+1], segment_tree[2*v+2])
def main():
    n=int(input())
    nums = list(map(int, input().split()))[:n]
    segment_tree = [0]*4*n
    build(0, 0, n, segment_tree, nums)
    q = int(input())
    res = []
    while q!=0:
        type_q, l, r = map(str,input().split())
        if type_q == "s":
            res.append(getMax(0, 0, n, segment_tree, int(l)-1, int(r)))
        else:
            update(0, 0, n, segment_tree, int(l)-1, int(r))
        q-=1
    print(*res)
main()

#МОД на подотрезках, поиск индекса максимума  2
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

def update(v, l, r, segment_tree, indx, value):
    if r-l == 1:
        segment_tree[v][0] = value
        return
    m = (l+r)//2
    if indx < m:
        update(2*v+1, l, m, segment_tree, indx, value)
    else:
        update(2*v+2, m, r, segment_tree, indx, value)
    segment_tree[v]=max(segment_tree[2*v+1], segment_tree[2*v+2])

def main():
    n=int(input())
    nums = list(map(int, input().split()))[:n]
    segment_tree = [[0,0]]*4*n
    build(0, 0, n, segment_tree, nums)
    q = int(input())
    res = []
    while q!=0:
        type_q, l, r = map(str,input().split())
        if type_q == "s":
            res.append(getMax(0, 0, n, segment_tree, int(l)-1, int(r)))
        else:
            update(0, 0, n, segment_tree, int(l)-1, int(r))
        q-=1
    for _, i in res:
        print(i+1, end = " ")
main()

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
    elif st_r[0] < st_l[0]:
        segm_tree[v] = st_l
    else:
        segm_tree[v] = [st_r[0], st_l[1]+st_r[1]]
def getMax(v, l, r, segm_tree, ql, qr):
    if ql <= l and qr >= r:
        return segm_tree[v]
    if ql>=r or qr<=l:
        return [-1e9, -1]
    m =(r+l)//2
    st_l=getMax(2*v+1, l, m, segm_tree, ql, qr)
    st_r = getMax(2*v+2, m, r, segm_tree, ql, qr)
    if st_l[0] > st_r[0]:
        return st_l
    elif st_l[0] < st_r[0]:
        return st_r
    else:
        return [st_r[0], st_l[1] + st_r[1]]

def update(v, l, r, segment_tree, indx, value):
      if r-l == 1:
         segment_tree[v][0] = value
         return
      m = (l+r)//2
      if indx < m:
          update(2*v+1, l, m, segment_tree, indx, value)
      else:
          update(2*v+2, m, r, segment_tree, indx, value)
      st_l = segment_tree[2*v+1]
      st_r=segment_tree[2*v+2]
      if st_l[0] > st_r[0]:
          segment_tree[v] = st_l
      elif st_l[0] < st_r[0]:
          segment_tree[v] = st_r
      else:
          segment_tree[v] = [st_r[0], st_l[1] + st_r[1]]
      segment_tree[v]=max(segment_tree[2*v+1], segment_tree[2*v+2])

def main():
    n=int(input())
    nums = list(map(int, input().split()))[:n]
    segment_tree = [[0,0]]*4*n
    build(0, 0, n, segment_tree, nums)
    q = int(input())
    res = []
    while q!=0:
        type_q, l, r = map(str,input().split())
        if type_q == "s":
            res.append(getMax(0, 0, n, segment_tree, int(l)-1, int(r)))
        else:
            update(0, 0, n, segment_tree, int(l)-1, int(r))
        q-=1
    for _, i in res:
        print(i, end = " ")
main()

# 5
# 1 3 2 3 3
# 5
# s 1 4
# u 3 3
# s 1 5
# u 2 1
# s 1 5