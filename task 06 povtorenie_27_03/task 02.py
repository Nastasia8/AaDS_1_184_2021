a = list(i for i in input().split(" "))
stack = []

op = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: y - x,
    '*': lambda x, y: x * y
}

for i in a:
    if i.isdigit():
        stack.append(int(i))
    else:
        stack.append(op[i](stack.pop(), stack.pop()))

print(stack[0])
