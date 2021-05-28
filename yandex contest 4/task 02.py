from collections import deque
size = int(input())
a = deque(list(map(int, input().split(" ")))[:size])
b = []
deadblock = []
res = list(range(1, size+1))
while a:
    if not deadblock or deadblock[-1] > a[0]:
        deadblock.append(a.popleft())
    if a and deadblock[-1] < a[0]:
        b.append(deadblock.pop())
while deadblock:
    b.append(deadblock.pop())

if res == b:
    print("YES")
else:
    print("NO")
