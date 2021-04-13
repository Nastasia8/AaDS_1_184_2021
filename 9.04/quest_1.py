def is_pos(string):
    pass

string = input().replace(" ", "")
stack = []
res_string = []
operations = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

for item in string:
    if item == ")":
        while stack[-1][0] = "(":
            res_string.append(stack.pop()[0])
        stack.pop()
        continue
    while stack and stack[-1][1] >= operations[item] and item != "(":
        res_string.append(stack.pop()[0])
    if not stack or stack[-1][1] < operations[item] or item == "(":
        stack.append([item, operations])

print(*res_string)

# in process