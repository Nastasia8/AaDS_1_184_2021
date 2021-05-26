def merge_sort(arr):
    global s
    if len(arr) > 1:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]
        merge_sort(left)
        merge_sort(right)

        a, b, c = 0, 0, 0
        while a < len(right) and b < len(left):  # Начиннаем объдинять части в один список
            if right[a] < left[b]:
                arr[c] = right[a]
                a += 1
                s += len(left)-b
            else:
                arr[c] = left[b]
                b += 1
            c += 1
        while b < len(left):  # Добавляем остатки литса в конец списка
            arr[c] = left[b]
            c += 1
            b += 1
        while a < len(right):  # Добавляем остатки листа в конец списка
            arr[c] = right[a]
            c += 1
            a += 1
    return arr


n = int(input())
arr = list(map(int, input().split()))[:n]
s = 0
merge_sort(arr)
print(s)