  
def func(s):
    c = 0
    k = []
    for i in s:
        if (i == '('):
            k.append(i)
        elif (k != []) and (k[-1] == '('):
            k.pop()
        else:
            c += 1
    return c+len(k)

s = str(input())
print(func(s))