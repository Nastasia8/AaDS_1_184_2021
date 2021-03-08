def funct(array):
    for arr in array:
        for j in range(len(arr)//2):
            arr[j], arr[-j-1]=arr[-j-1], arr[j]
    return array
array = [[2, 5, 4], [3, 1, 9,], [8, 7, 6]]
print(funct(array))
