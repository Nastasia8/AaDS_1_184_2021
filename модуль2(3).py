def sort(a, start, end):
    if len(a) > 1:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]

        sort(left, start, start + mid - 1)
        sort(right, start + mid, end)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1

        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
        print(start, end, a[0], a[-1])
    return a

n = int(input())
a = list(map(int, input().split()))[:n]
sort(a, 1, len(a))
print(*a)
