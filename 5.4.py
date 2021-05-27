#функция построения дерева отрезков
def build(v, l, r, t, a):
    if r-l == 1:
        t[v] = a[l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, t, a)
    build(2*v+2, m, r, t, a)
    t[v] = t[2*v+1] + t[2*v+2]
# функция поиска нулей
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
# функция для запроса суммы, в которую передается информация о текущей вершине дерева
def get_sum(v, l, r, t, ql, qr):
    if ql <= l and qr >= r:
        return t[v]
    if ql >= r or qr <= l:
        return 0
    m = (r+l)//2
    tl = get_sum(2*v+1, l, m, t, ql, qr)
    tr = get_sum(2*v+2, m, r, t, ql, qr)
    return tl + tr

n = int(input())
a = [0 if int(i) != 0 else 1 for i in input().split()]
do = [0]*4*n
build(0, 0, n, do, a)
q = int(input())
index = []
while q != 0:
    l, r, k = map(int, input().split())
    sum_ = get_sum(0, 0, n, do, l-1, r)
    if sum_ >= k and l > 1:
        index.append(get_k_zero(0, 0, n, do, k+get_sum(0, 0, n, do, 0, l-1)))
    elif sum_ >= k and l == 1:
        index.append(get_k_zero(0, 0, n, do, k))
    else:
        index.append(-1)
    q -= 1
print(*index)