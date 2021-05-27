def build(v,l,r,segment_tree, x):  #создаем функцию с переменными 
    if r - l == 1:
        segment_tree[v]= x[l]
        return
    m=(r+l)//2
    build(2*v+1,l,m,segment_tree,x)
    build(2*v+2,m,r,segment_tree,x)
    segment_tree[v] = (segment_tree[2*v+1]+segment_tree[2*v+2])

def getSum(v,l,r,segment_tree,ql,qr): #функция, которая находит сумму 
    if ql<=l and qr>=r:
        return segment_tree[v]
    if ql >= r or qr<=l:
        return 0
    m = (r+l)//2
    st_l = getSum (2*v+1,l,m,segment_tree,ql,qr)
    st_r = getSum (2*v+2,m,r,segment_tree,ql,qr)
    return st_l + st_r

def findK(v, l, r, segment_tree, k): #функция, которая ищет нули
    if k > segment_tree[v]:
        return -1
    if r - l == 1:
        return r
    m = (r+l)//2
    if segment_tree[2*v+1] >= k:
        return findK(2*v+1, l, m, segment_tree, k)
    else:
        return findK(2*v+2, m, r, segment_tree, k - segment_tree[2*v+1])

def main():
    number =int(input())
    x = [1 if int(i)==0 else 0 for i in input().split()]
    segment_tree = [0]*4*number
    build(0,0,number,segment_tree, x)
    q = int(input())
    ind = []
    while q !=0:
        l,r,k = map(int, input().split())
        sum = getSum(0, 0, number, segment_tree, l-1, r)
        if sum >= k and l == 1:
            ind.append(findK(0, 0, number, segment_tree, k))
        elif sum >= k and l > 1:
            ind.append(findK(0, 0, number, segment_tree, k +(getSum(0, 0, number, segment_tree, 0, l-1))))
        else:
            ind.append(-1)
        q-=1
    print(*ind)


main()