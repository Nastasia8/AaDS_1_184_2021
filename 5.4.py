def build(value, left, right, segments_tree, numbers): #строит дерево
    if right - left == 1:
        segments_tree[value] = numbers[left]
        return

    middle = (right + left) // 2

    build(2 * value + 1, left, middle, segments_tree, numbers)
    build(2 * value + 2, middle, right, segments_tree, numbers)

    segments_tree[value] = segments_tree[2 * value + 1] + segments_tree[2 * value + 2]

def get_k_zero(value, left, right, segments_tree, number): # ищем k-ноль
    if number > segments_tree[value]:
        return -1
    if right - left == 1:
        return right

    middle = (right + left) // 2

    if segments_tree[2 * value + 1] >= number:
        return get_k_zero(2 * value + 1, left, middle, segments_tree, number)
    else:
        return get_k_zero(2 * value + 2, middle, right, segments_tree, number - segments_tree[2 * value + 1])

def get_sum(value, left, right, segments_tree, q_left, q_right): #ищем сумму
    if q_left <= left and q_right >= right:
        return segments_tree[value]

    if q_left >= right or q_right <= left:
        return 0

    middle = (right + left) // 2

    t_left = get_sum(2 * value + 1, left, middle, segments_tree, q_left, q_right)
    t_right = get_sum(2 * value + 2, middle, right, segments_tree, q_left, q_right)

    return t_left + t_right

n = int(input())
numbers = [0 if int(i) != 0 else 1 for i in input().split()] # лист для следующей работы


segments_tree = [0] * 4 * n

build(0, 0, n, segments_tree, numbers)
q = int(input())
res = []

while q != 0:
    left, right, number = map(int, input().split()) # входные данные
    sum = get_sum(0, 0, n, segments_tree, left - 1, right)# получаем сумму
    if sum >= number and left > 1: # если сумма > данных и левый элемент > 1 - добавить k_zero + sum
        res.append(get_k_zero(0, 0, n, segments_tree, number + get_sum(0, 0, n, segments_tree, 0, left - 1)))
    elif sum >= number and left == 1:  # если сумма > данных и левый элемент == 1 - добавить k_zero
        res.append(get_k_zero(0, 0, n, segments_tree, number))
    else: # иначе добавить -1
        res.append(-1)
    q -= 1

print(*res) # выводим, * обозначает, что объектов может быть несколько
