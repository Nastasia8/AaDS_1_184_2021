a = list(range(1, 26)) #1 способ
new_start=a.pop()
new_end=a.pop(0)
a.append(new_end)
a.insert(0, new_start)
print(a)

def funny(num): #2 способ
    num[0], num[-1] = num[-1], num[0]
    return num
a = list (range(1,26))
print(funny(a))
