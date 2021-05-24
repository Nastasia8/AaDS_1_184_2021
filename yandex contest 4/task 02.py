# Мое решение у которого ошибка в 8 тесте

from collections import deque
size = int(input())
a = deque(list(map(int, input().split(" ")))[:size])
inOrder = True

for _ in range(len(a)):
    if a[0] == max(a) or a[0] == min(a):
        a.popleft()
    else:
        inOrder = False
        break

print("YES" if inOrder else "NO")

# Решение которое вы мне показали

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
