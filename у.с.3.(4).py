def inversion(M, invers):

    if len(M) > 1:
        mid = len(M)//2
        left = M[:mid]
        right = M[mid:]
        
        invers = inversion(left, invers)
        invers = inversion(right, invers)

        i,j,k = 0,0,0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                M[k] = left[i]
                i += 1
            else:
                M[k] = right[j]
                j = j+1
                invers += len(left)-i
            k = k+1
        while i < len(left):
            M[k] = left[i]
            i = i+1
            k = k+1
        while j < len(right):
            M[k] = right[j]
            j = j+1
            k = k+1

    return invers


invers = 0
n = int(input())
M = list(map(int, input().split()))[:n]
invers = inversion(M, invers)
print(invers)