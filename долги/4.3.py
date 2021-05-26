b = int(input())
num = list(map(int, input().split()))[:b]
stack = []
indexes = [0]*b
for i in range(b-1, -1, -1):
    while stack and num[stack[-1]] >= num[i]:
        stack.pop()
    indexes[i] = stack[-1] if stack else -1
    stack.append(i)

[print(item) for item in indexes]