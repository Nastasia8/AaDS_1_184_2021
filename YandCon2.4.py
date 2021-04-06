def merge_sort(arr, lst):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        lst = merge_sort(left, lst)
        lst = merge_sort(right, lst)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j = j + 1
                lst += len(left) - i
            k = k + 1
        while i < len(left):
            arr[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            arr[k] = right[j]
            j = j + 1
            k = k + 1
    return lst
lst = 0
n = int(input())
arr = list(map(int, input().split()))
print(merge_sort(arr, lst))
