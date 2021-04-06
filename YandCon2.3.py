def merge(arr, lst):
    new_lst = [] 
    i = 0
    j = 0
    while i < len(arr) and j < len(lst):
        if arr[i] < lst[j]:
            new_lst.append(arr[i])
            i += 1
        else:
            new_lst.append(lst[j])
            j += 1
    while i < len(arr):   
        new_lst.append(arr[i])
        i += 1
    while j < len(lst):
        new_lst.append(lst[j])
        j += 1

    return new_lst 

def mergeSort(arr, index):
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr)//2
        left = mergeSort(arr[:mid], [index[0],index[0]+mid])
        right = mergeSort(arr[mid:],[index[0]+mid, index[1]]) 

        sort = merge(left, right)
        print(index[0]+1, index[1], sort[0], sort[-1])  
        return sort

k = int(input())
arr = list(map(int, input().split())) 
arr = mergeSort(arr,[0, k])
print(' '.join(map(str, arr)))