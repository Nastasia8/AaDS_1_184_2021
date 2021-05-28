a,b = map(int, input().split())
nums =[int(i) for i in input().split()]
stack = []
res=[0]*a
for i in range(a):
    while stack and nums[stack[-1]] > nums[i]:
        res[stack.pop()] = i
    stack.append(i)
while stack:
    res[stack.pop()]=a
minIndx = 0
for i in range(a-b+1):
    if minIndx<i:
        minIndx=i
    while res[minIndx]<i+b:
        minIndx= res[minIndx]
    print(nums[minIndx])