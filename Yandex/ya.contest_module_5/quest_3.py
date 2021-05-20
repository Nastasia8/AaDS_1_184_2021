def NOD(a, b):
    while b:
        a, b = b, a % b
    return a

def build(v, left, right, segment_tree, nums):
    if right - left == 1:
        segment_tree[v] = nums[left]
        return
    middle = (left + right) // 2
    build(2 * v + 1, left, middle, segment_tree, nums)
    build(2 * v + 2, middle, right, segment_tree, nums)
    segment_tree[v] = NOD(segment_tree[2 * v + 1], segment_tree[2 * v + 2])


def get_NOD(v, left, right, segment_tree, q_left, q_right):
    if q_left <= left and q_right >= right:
        return segment_tree[v]
    if q_left >= right or q_right <= left:
        return 0
    middle = (left + right) // 2
    st_l = get_NOD(2 * v + 1, left, middle, segment_tree, q_left, q_right)
    st_r = get_NOD(2 * v + 2, middle, right, segment_tree, q_left, q_right)
    return NOD(st_l, st_r)

n = int(input())
numbers = list(map(int, input().split()))[:n]
segment_tree = [0] * 4 * n
build(0, 0, n, segment_tree, numbers)
q = int(input())
res = []
while q != 0:
    left, right = map(int, input().split())
    res.append(get_NOD(0, 0, n, segment_tree, left - 1, right))
    q -= 1

print(*res)
