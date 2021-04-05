def func(s):
    count = 0
    n = []
    for i in s:
        if (i == '('):
            n.append(i)
        elif (n != []) and (n[-1] == '('):
            n.pop()
        else:
            count += 1
    return count+len(n)

s = str(input())
print(func(s))
