# можно не смотреть, мои попытки ломать и учить код...))
def build(v, left, right, segment_tree, nums):
    if right - left == 1:
        segment_tree[v] = [nums[left], 1]
        return
    middle = (right + left)//2
    build(2*v+1, left, middle, segment_tree, nums)
    build(2*v+2, middle, right, segment_tree, nums)
    segment_tree[v] = max(segment_tree[2*v +1], segment_tree[2*v + 2])
    t_left = segment_tree[2*v + 1]
    t_right = segment_tree[2*v + 2]
    if t_left[0] > t_right[0]:
        segment_tree[v] = t_left
    elif t_left[0] < t_right[0]:
        segment_tree[v] = t_right
    else:
        segment_tree[v] = [t_right[0], t_right[1] + t_left[1]]


def getMax(v, left, right, segment_tree, q_left, q_right):
    if q_left <= left and q_right >= right:
        return segment_tree[v]
    if q_left >= right or q_right <= left:
        return [-1e9, -1]
   # middle = (right + left) // 2
    tl = getMax(2*v +1, left, middle, segment_tree, q_left, q_right)
    tr = getMax(2 * v + 2, middle, right, segment_tree, q_left, q_right)
    if tl[0] > tr[0]:
        return tl
    elif tl[0] < tr[0]:
        return tr
    else:
        return [tr[0], tr[1] + tl[1]]

def update(v, left, right, segment_tree, ind_x, value):
    if right - left == 1:
        segment_tree[v][0] = value 
        return
    middle = (left + right) // 2
    if ind_x < middle:
        update(2 * v + 1, left, middle, segment_tree, ind_x, value)
    else:
        update(2 * v + 2, middle, right, segment_tree, ind_x, value)
    t_left = segment_tree[2*v + 1]
    t_right = segment_tree[2*v + 2]
    if t_left[0] > t_right[0]:
        segment_tree[v] = t_left
    elif t_left[0] < t_right[0]:
        segment_tree[v] = t_right
    else:
        segment_tree[v] = [t_right[0], t_right[1] + t_left[1]]

def main():
    n = int(input())
    numbers = list(map(int, input().split()))[:n]
    segment_tree = [[0, 0]]*(4*n)
   # build(0, 0, n, segment_tree, numbers)
    q = int(input())
    array = []
    while q != 0:
        type_q, left, right = map(str, input().split())
        if type_q == 's':
            array.append(getMax(0, 0, n, segment_tree, int(left)-1, int(right)))
        else:
            update(0, 0, n, segment_tree, int(left) - 1, int(right)) # left - index, right - rename value
        q -= 1
    for _, i in array:
        print(i, end=" ")

main()