from math import gcd

def build(v, l, r, segment_tree, number): #создаем функцию c переменными
    if r-l == 1:
        segment_tree[v] = number[l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, segment_tree, number)
    build(2*v+2, m, r, segment_tree, number)
    segment_tree[v] = gcd(segment_tree[2*v+1], segment_tree[2*v+2])

def calc(v, l, r, segment_tree, ql, qr): #считаем НОД слева и справа
    if ql <= l and qr >= r:
        return segment_tree[v]
    if ql >= r or qr <= l:
        return 0
    m = (r+l)//2
    tl = calc(2*v+1, l, m, segment_tree, ql, qr)
    tr = calc(2*v+2, m, r, segment_tree, ql, qr)
    return gcd(tl, tr)

def main():
    n = int(input()) 
    number = list(map(int, input().split())) 
    segment_tree = [0]*4*n
    build(0, 0, n, segment_tree, number)
    q = int(input())
    index = []
    while q != 0: 
        l, r = map(int, input().split())
        index.append(calc(0, 0, n, segment_tree, l-1, r))
        q -= 1
    print(*index)

main()