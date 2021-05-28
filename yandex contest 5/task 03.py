from math import gcd # из библиотеки math добавить функйию наибольшего общего делителя

def build(v, l, r, do, a): # построить подотрезок
    if r-l == 1:
        do[v] = a[l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, do, a)
    build(2*v+2, m, r, do, a)
    do[v] = gcd(do[2*v+1], do[2*v+2])

def get_gcd(v, l, r, do, ql, qr): # найти наибольший общий делитель
    if ql <= l and qr >= r:
        return do[v]
    if ql >= r or qr <= l:
        return 0
    m = (r+l)//2
    tl = get_gcd(2*v+1, l, m, do, ql, qr)
    tr = get_gcd(2*v+2, m, r, do, ql, qr)
    return gcd(tl, tr) # вернуть наибольший делитель

n = int(input()) # колличество элементов в отрезке
a = list(map( int, input().split())) # запросы
do=[0]*4*n
build(0, 0, n, do, a) # построить подотрезок
q = int(input()) # колличество запросов
index = [] # ответ
while q != 0: # пока есть запросы
    l, r = map(int, input().split()) # граница слева и справа
    index.append(get_gcd(0, 0, n, do, l-1, r)) # найти наибольший общий делитель и присоеденить к массиву ответов
    q -= 1 # уменьшить колличество запросов
    
print(*index) # вывести ответ
