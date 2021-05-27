stack=[]
a=input()
b=0
for i in a:
    if i==")":
        if not stack or stack [-1]!="(":
            b+=1
            continue
        stack.pop()
    else:
        stack.append(i)
        

print(b+len(stack))