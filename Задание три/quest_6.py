
def func(lst):
    for item in range(len(lst)):
        count = lst.count(lst[item])
        if count > 1:
            lst[item] = str(lst[item])*count
    return set(lst)

first_list = [1, 3, 7, 18, 9, 9, 3, 5, ]

print(func(first_list))

