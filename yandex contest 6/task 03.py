from heapq import heapify, heappop

size = int(input())
a = list(-int(i) for i in input().split(" "))[:size]
b = [-int(i) for i in a]
b.sort()

while a:
    heapify(a)
    print(*[-int(i) for i in a])
    heappop(a)

print(*b)
