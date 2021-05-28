def MergeSort(num, start, end):
    if end - start > 1:
        mid = (end + start)//2
        MergeSort(num, start, mid)
        MergeSort(num, mid, end)
        left = num[start:mid]
        right = num[mid:end]
        internal_sort(num, left, right,start)
        print(start + 1, end, num[start], num[end - 1])
def internal_sort(arr, left, right, start):
    i = j = 0
    k = start
    while i < len(right) and j < len(left):
        if left[j] > right[i]:
            arr[k]= right[i]
            i += 1
        else:
            arr[k] = left[j]
            j += 1
        k +=1
    while j < len(left):
        arr[k] = left[j]
        j += 1
        k += 1
    while i < len(right):
        arr[k] = right[i]
        i += 1
        k += 1

def main():
    n = int(input())
    numbers = list(map(int, input().split()))[:n]
    MergeSort(numbers, 0, len(numbers))
    print(" ".join(map(str, numbers)))
main()