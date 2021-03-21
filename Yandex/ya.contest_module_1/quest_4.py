def Sort(array, numbers):
    list_ = [0]*numbers
    return merge_sort(array, list_, 0, numbers-1)

def merge_sort(array, list_, left, right):
    count = 0
    if left < right:
        middle = (left + right)//2
        count += merge_sort(array, list_, left, middle)
        count += merge_sort(array, list_, middle + 1, right)
        count += Merge(array, list_, left, middle, right)
    return count

def Merge(array, list_, left, middle, right):
    i = left     
    j = middle + 1 
    k = left     
    count = 0
    while left <= middle and j <= right:
        if array[i] <= array[j]:
            list_[k] = array[i]
            k += 1
            i += 1
        else:
            list_[k] = array[j]
            count += (middle-i + 1)
            k += 1
            j += 1
    while i <= middle:
        list_[k] = array[i]
        k += 1
        i += 1
    while j <= right:
        list_[k] = array[j]
        k += 1
        j += 1
    for item in range(left, right + 1):
        array[item] = list_[item]    
    return count

Leght = int(input())
array = list(map(int, input().split())) 
numbers = len(array)
array = Sort(array, numbers)
print(array) 
