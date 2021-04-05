#акая-то задача
s=input()
stack=[]
isPsp=True
for i in s:
    if i==")":
        if not stack or stack[-1]!="(":
            isPsp=False
            break
        stack.pop()
    elif i=="]":
        if not stack or stack[-1]!="[":
            isPsp=False
            break
        stack.pop()
    elif i=="}":
        if not stack or stack[-1]!="{":
            isPsp=False
            break
        stack.pop()
    else:
        stack.append(i)
if isPsp and not stack:
    print("Yes")
else:
    print("No")
#еще какая-то задача
stack = []
for i in input().split():
    if i in '+-*':
        a = stack[-2]
        b = stack[-1]
        stack.pop()
        stack.pop()
        if i == '+':
            result = a + b
        elif i == '-':
            result = a - b
        else:
            result = a * b
        stack.append(result)
    else:
        stack.append(int(i))
print(stack[0])
#и еще какая-то задача
s = input().replace(" ", "")
stack = []
for i in s:
    if i.isdigit():
        stack.append(int(i))
    else:
        d2 = stack.pop()
        d1 = stack.pop()
        if i == '+':
            stack.append(d1+d2)
        elif i == '-':
            stack.append(d1-d2)
        else:
            stack.append(d1*d2)
print(stack[0])
