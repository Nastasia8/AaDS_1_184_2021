def func(x,y,z,segment_tree,numbers):
    if z - y == 1:
        segment_tree[x]= numbers[y]
        return
    m=(z+y)//2
    func(2*x+1,y,m,segment_tree,numbers)
    func(2*x+2,m,z,segment_tree,numbers)
    segment_tree[x] = (segment_tree[2*x+1]+segment_tree[2*x+2])

def getSum(x,y,z,segment_tree,qy,qz): #функция, которая находит сумму
    if qy<=y and qz>=z:
        return segment_tree[x]
    if qy >= z or qz<=y:
        return 0
    m = (z+y)//2
    st_y = getSum (2*x+1,y,m,segment_tree,qy,qz)
    st_z = getSum (2*x+2,m,z,segment_tree,qy,qz)
    return st_y + st_z

def findK(x, y, z, segment_tree, k): #функция,которая находит нули
    if k > segment_tree[x]:
        return -1
    if z - y == 1:
        return z
    m = (z+y)//2
    if segment_tree[2*x+1] >= k:
        return findK(2*x+1, y, m, segment_tree, k)
    else:
        return findK(2*x+2, m, z, segment_tree, k - segment_tree[2*x+1])

def main():
    n=int(input())
    numbers= [1 if int(i)==0 else 0 for i in input().split()]
    segment_tree = [0]*4*n
    func(0,0,n,segment_tree,numbers)
    q = int(input())
    arr = []
    while q !=0:
        y,z,k = map(int, input().split())
        sum = getSum(0, 0, n, segment_tree, y-1, z)
        if sum >= k and y == 1: #Выводим К-ый слева 0 элемент
            arr.append(findK(0, 0, n, segment_tree, k))
        elif sum >= k and y > 1:
            arr.append(findK(0, 0, n, segment_tree, k +(getSum(0, 0, n, segment_tree, 0, y-1))))
        else:
            arr.append(-1) #Если индекса не сущ-ет, выводим -1
        q-=1
    print(*arr)


main() 