def build(v, l, r, t, a):
    if r-l == 1:
        t[v] = a[l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, t, a)
    build(2*v+2, m, r, t, a)
    t[v] = t[2*v+1] + t[2*v+2]

def get_k_zero(v, l, r, t, k):
    if k > t[v]:
        return -1
    if r - l == 1:
        return r
    m = (r+l)//2
    if t[2*v+1] >= k:
        return get_k_zero(2*v+1, l, m, t, k)
    else:
        return get_k_zero(2*v+2, m, r, t, k - t[2*v+1])

def get_sum(v, l, r, t, ql, qr):
    if ql <= l and qr >= r:
        return t[v]
    if ql >= r or qr <= l:
        return 0
    m = (r+l)//2
    tl = get_sum(2*v+1, l, m, t, ql, qr)
    tr = get_sum(2*v+2, m, r, t, ql, qr)
    return tl + tr
# то же, что и в 4 задаче, ноо
# по умному: функция запроса модификации,
# передается информация о текущей вершине дерева отрезков,
# дополнительно указывается индекс меняющегося элемента и его новое значение
def update(v, l, r, t, idx, value):
    if r-l == 1:
        t[v] = value
        return
    m = (r+l)//2
    if idx < m:
        update(2*v+1, l, m, t, idx, value)
    else:
        update(2*v+2, m, r, t, idx, value)
    t[v] = t[2*v+1] + t[2*v+2]

n = int(input())
a = [0 if int(i) != 0 else 1 for i in input().split()]
t = [0]*4*n
build(0, 0, n, t, a)
q = int(input())
index = []
while q != 0:
    input_ = input().split()
    if len(input_) == 4:
        l, r, k = int(input_[1]), int(input_[2]), int(input_[3])
        sum_ = get_sum(0, 0, n, t, l-1, r)
        if sum_ >= k and l > 1:
            index.append(get_k_zero(0, 0, n, t, k+get_sum(0, 0, n, t, 0, l-1)))
        elif sum_ >= k and l == 1:
            index.append(get_k_zero(0, 0, n, t, k))
        else:
            index.append(-1)
    else:
        i, v = int(input_[1]), int(input_[2])
        if v == 0:
            update(0, 0, n, t, i-1, 1)
        else:
            update(0, 0, n, t, i-1, 0)
    q -= 1
print(*index)