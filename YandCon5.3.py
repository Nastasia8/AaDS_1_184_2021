def nod(a,b):
    while b:
        a, b = b, a % b
    return a

def build(v, l, r, segment_tree, nums):
    if r - l == 1:
        segment_tree[v] = nums[l]
        return
    m = (r + l) // 2
    build(2 * v + 1, l, m, segment_tree, nums)
    build(2 * v + 2, m, r, segment_tree, nums)
    segment_tree[v] = nod(segment_tree[2 * v + 1], segment_tree[2 * v + 2])


def getNOD(v, l, r, segment_tree, ql, qr):
    if ql <= l and qr >= r:
        return segment_tree[v]
    if ql >= r or qr <= l:
        return 0
    m = (r + l) // 2
    st_l = getNOD(2 * v + 1, l, m, segment_tree, ql, qr)
    st_r = getNOD(2 * v + 2, m, r, segment_tree, ql, qr)
    return nod(st_l, st_r)


def main():
    n = int(input())
    numbers = list(map(int, input().split()))[:n]
    segment_tree = [0] * 4 * n
    build(0, 0, n, segment_tree, numbers)
    q = int(input())
    arr = []
    while q != 0:
        l, r = map(int, input().split())
        arr.append(getNOD(0, 0, n, segment_tree, l - 1, r))
        q -= 1
    print(*arr)


main()
