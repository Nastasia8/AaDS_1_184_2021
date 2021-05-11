def func(s):
    Counter = 0
    lst = []
    for i in s:
        if (i == '('):
            lst.append(i)
        elif (lst != []) and (lst[-1] == '('):
            lst.pop()
        else:
            Counter += 1
    return Counter+len(lst)

s = str(input())
print(func(s))
