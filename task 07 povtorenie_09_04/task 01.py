def is_pos(s):
    stack = []
    for i in s:
        if i.isdigit():
            stack.append(int(i))
        else:
            n2 = stack.pop()
            n1 = stack.pop()
            if i == "+":
                stack.append(n1 + n2)
            elif i == "-":
                stack.append(n1 - n2)
            elif i == "*":
                stack.append(n1 * n2)
            else:
                stack.append(n1 // n2)
    print(stack[-1])

s = input().replace(" ", "")
stack = []
res_string = []
operations = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
i = 0
while i < len(s):
    if s[i] in "+-*/()":
        if s[i] == ")":
            while stack[-1][0] != "(":
                res_string.append(stack.pop()[0])
            stack.pop()
            i += 1
            continue
        while stack and stack[-1][1] >= operations[s[i]] and s[i] != "(":
            res_string.append(stack.pop()[0])
        if not stack or stack[-1][1] < operations[s[i]] or s[i] == "(":
            stack.append([s[i], operations[s[i]]])
        i += 1
    else:
        str_digit = ""
        while i < len(s) and s[i].isdigit():
            str_digit += s[i]
            i += 1
        res_string.append(str_digit)
while stack:
    res_string.append(stack.pop()[0])

print(*res_string)
is_pos(res_string)
