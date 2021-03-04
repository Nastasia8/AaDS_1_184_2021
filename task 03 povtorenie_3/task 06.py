a = [5, 6, 9, 6, 3, 5, 2, 5, 1]

def func(list):
    for i in range(0, len(list)):
        for j in range(0, i):
            if list[i] == list[j]:
                list[i] = list[i] * 10 + list[i] % 10
    return(set(a))

print(func(a))
