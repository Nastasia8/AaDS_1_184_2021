def build(v, l, r, segment_tree, nums):
    if r - l == 1:
        segment_tree[v] = nums[l]
        return
    m = (r + l) // 2
    build(2 * v + 1, l, m, segment_tree, nums)
    build(2 * v + 2, m, r, segment_tree, nums)
    segment_tree[v] = (segment_tree[2 * v + 1] + segment_tree[2 * v + 2])


def getSum(v, l, r, segment_tree, ql, qr):
    if ql <= l and qr >= r:
        return segment_tree[v]
    if ql >= r or qr <= l:
        return 0
    m = (r + l) // 2
    st_l = getSum(2 * v + 1, l, m, segment_tree, ql, qr)
    st_r = getSum(2 * v + 2, m, r, segment_tree, ql, qr)
    return st_l + st_r


def findK(v, l, r, segment_tree, k):
    if k > segment_tree[v]:
        return -1
    if r - l == 1:
        return r
    m = (r + l) // 2
    if segment_tree[2 * v + 1] >= k:
        return findK(2 * v + 1, l, m, segment_tree, k)
    else:
        return findK(2 * v + 2, m, r, segment_tree, k - segment_tree[2 * v + 1])


def update(v, l, r, segment_tree, indx, value):
    if r - l == 1:
        segment_tree[v] = value
        return
    m = (l + r) // 2
    if indx < m:
        update(2 * v + 1, l, m, segment_tree, indx, value)
    else:
        update(2 * v + 2, m, r, segment_tree, indx, value)
    segment_tree[v] = segment_tree[2 * v + 1] + segment_tree[2 * v + 2]


def main():
    n = int(input())
    numbers = [1 if int(i) == 0 else 0 for i in input().split()]
    segment_tree = [0] * 4 * n
    build(0, 0, n, segment_tree, numbers)
    q = int(input())
    arr = []
    while q != 0:
        i = input().split()
        if len(i) == 4:
            left, right, number = int(i[1]), int(i[2]), int(i[3])
            sum = getSum(0, 0, n, segment_tree, left - 1, right)
            if sum >= number and left > 1:
                arr.append(findK(0, 0, n, segment_tree, number + getSum(0, 0, n, segment_tree, 0, left - 1)))
            elif sum >= number and left == 1:
                arr.append(findK(0, 0, n, segment_tree, number))
            else:
                arr.append(-1)
        else:
            i, v = int(i[1]), int(i[2])
            if v == 0:
                update(0, 0, n, segment_tree, i - 1, 1)
            else:
                update(0, 0, n, segment_tree, i - 1, 0)
        q-=1
    print(*arr)

main()