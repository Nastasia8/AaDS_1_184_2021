def merge_sort(num, a):
    if len(num) > 1:
        middle = len(num) // 2
        left = num[:middle]
        right = num[middle:]
        a = merge_sort(left, a)
        a = merge_sort(right, a)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                num[k] = left[i]
                i += 1
            else:
                num[k] = right[j]
                j = j + 1
                a += len(left) - i
            k = k + 1
        while i < len(left):
            num[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            num[k] = right[j]
            j = j + 1
            k = k + 1
    return a
def main():
    end = 0
    n = int(input())
    num = list(map(int, input().split()))[:n]
    print(merge_sort(num, end))
main()