def merge_sort(mas, kt):
    if len(mas) > 1:
        middle = len(mas) // 2
        left = mas[:middle]
        right = mas[middle:]
        kt = merge_sort(left, kt)
        kt = merge_sort(right, kt)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                mas[k] = left[i]
                i += 1
            else:
                mas[k] = right[j]
                j = j + 1
                kt += len(left) - i
            k = k + 1
        while i < len(left):
            mas[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            mas[k] = right[j]
            j = j + 1
            k = k + 1
    return kt
kt = 0
n = int(input())
mas = list(map(int, input().split()))
print(merge_sort(mas, kt)) 