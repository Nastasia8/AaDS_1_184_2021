#1 способ
a = list(range(1, 26))
new_start=a.pop()
new_end=a.pop(0)
a.append(new_end)
a.insert(0, new_start)
print(a)
#2 способ 
def funny(w):
    w[0], w[-1] = w[-1], w[0]
    return w
a = list (range(1,26))
print(funny(a))
