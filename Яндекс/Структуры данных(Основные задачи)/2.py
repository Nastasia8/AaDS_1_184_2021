n = input()
a = list(map(int, input().split()))
b = []
stack = []
k = 1
for i in a:
    if i != k:
        stack.append(i)
    b.append(i)
    k += 1
    for z in range(len(stack)):
        if stack[-1] == k:
            b.append(k)
            stack.pop()
            k += 1
if b[-1] == n:
    print("YES")
else:
    print("NO")