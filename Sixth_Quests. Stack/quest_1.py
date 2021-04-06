string = input()

stack = []

ispsp = True

for i in string:
    if i == ")":
        if not stack or stack[-1] != "(":
            ispsp = False
            break
        stack.pop()
    elif i == "]":
        if not stack or stack[-1] != "[":
            ispsp = False
            break
        stack.pop()
    elif i == "}":
        if not stack or stack[-1] != "{":
            ispsp = False
            break
        stack.pop()
    else:
        stack.append(i)

if ispsp and not stack:
    print('YES')
else:
    print('NO')

