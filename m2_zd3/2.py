def merge_sort(numbers, start, end):
    b=[]
    b=numbers.copy()
    if end - start > 1:
        mid = (start + end)//2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        print(start + 1, end, b[end - 1], b[start])
        merge_list(numbers, start, mid, end)
def merge_list(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            numbers[k] = left[i]
            i = i + 1
        else:
            numbers[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            numbers[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            numbers[k] = right[j]
            j = j + 1
            k = k + 1
def main():
    n=int(input())
    numbers=list(map(int,input().split()))[:n]
    merge_sort(numbers,0,len(numbers))
    print(" ".join(map(str,numbers)))
main()