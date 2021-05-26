def nod(a,b):
    while b:
        a, b = b, a % b
    return a

def build(v, left, rigcht, segment_tree, nums):
    if rigcht - left == 1:
        segment_tree[v] = nums[left]
        return
    middle = (rigcht + left) // 2
    build(2 * v + 1, left, middle, segment_tree, nums)
    build(2 * v + 2, middle, rigcht, segment_tree, nums)
    segment_tree[v] = nod(segment_tree[2 * v + 1], segment_tree[2 * v + 2])


def getNOD(v, left, rigcht, segment_tree, ql, qr):
    if ql <= left and qr >= rigcht:
        return segment_tree[v]
    if ql >= rigcht or qr <= left:
        return 0
    middle = (rigcht + left) // 2
    st_l = getNOD(2 * v + 1, left, middle, segment_tree, ql, qr)
    st_r = getNOD(2 * v + 2, middle, rigcht, segment_tree, ql, qr)
    return nod(st_l, st_r)


def main():
    n = int(input())
    numbers = list(map(int, input().split()))[:n]
    segment_tree = [0] * 4 * n
    build(0, 0, n, segment_tree, numbers)
    q = int(input())
    arr = []
    while q != 0:
        left, rigcht = map(int, input().split())
        arr.append(getNOD(0, 0, n, segment_tree, left - 1, rigcht))
        q -= 1
    print(*arr)


main()