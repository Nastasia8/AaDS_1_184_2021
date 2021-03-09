a =  (5, 1, 3, 5, 3, 1, 0, 9, 5, 3, 8, 6, 5, 7)
b = []
for ind, elements in enumerate (a):
    if elements == 5:
        b.append(ind)
print(b)
