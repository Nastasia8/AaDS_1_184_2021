def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers, 0
    middle = int( len(numbers) / 2 )
    left, a = merge_sort(numbers[:middle])
    right, b = merge_sort(numbers[middle:])
    result, c = internal_sort(left, right)
    return result, (a + b + c)

def internal_sort(left, right):
    result = []
    count = 0
    k,h = 0, 0
    left_len = len(left)
    while k < left_len and h < len(right):
        if left[k] <= right[h]:
            result.append(left[k])
            k += 1
        else:
            result.append(right[k])
            count += left_len - k
            h += 1
    result += left[k:]
    result += right[h:]
    return result, count


n = int(input())
numbers = list(map(int, input().split()))[:n]
print(merge_sort(numbers)[1])
