def sort(a, d):

    if len(a) > 1:
        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]
        
        d = sort(left, d)
        d = sort(right, d)

        i,j,k = 0,0,0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j = j+1
                d += len(left)-i
            k = k+1
        while i < len(left):
            a[k] = left[i]
            i = i+1
            k = k+1
        while j < len(right):
            a[k] = right[j]
            j = j+1
            k = k+1

    return d


d = input()
n = input()
a = list(map(int, input().split()))[:n]
sort(a, d)
print(d)