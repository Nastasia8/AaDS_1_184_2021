a=input()
stack=[]
for i in a:
    if not stack:
        stack.append(i)
    elif i==")" and stack[-1]=="(":
        stack.pop()
    else:
        stack.append(i)
print(len(stack))