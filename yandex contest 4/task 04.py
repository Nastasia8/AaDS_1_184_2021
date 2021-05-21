# Оба решения не проходят 3 тест на яндекс контесте (ошибка во время исполнения)

# Мое решение

from collections import deque
size, shift = map(int, input().split(" "))
a = deque(list(map(int, input().split(" ")))[:size])

for _ in range(size - shift + 1):
    print(min(a[i] for i in range(shift)), end=" ")
    a.popleft()
    
# Решение, которое писали на паре

n,k = map(int, input().split())
nums = list(int(i) for i in input().split(" "))
stack = []
res = [0] * n

for i in range(n):
    while stack and nums[stack[-1]] > nums[i]:
        res[stack.pop()] = i
    stack.append(i)

while stack:
    res[stack.pop()] = n
    
minIndx = 0

for i in range(n-k+1):
    if minIndx<i:
        minIndx=i
        
    while res[minIndx]<i+k:
        minIndx= res[minIndx]
        
    print(nums[minIndx])
