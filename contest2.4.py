def Inverion(N, invers):

    if len(N) > 1:
        mid = len(N)//2
        left = N[:mid]
        right = N[mid:]
        
        invers = Inverion(left, invers)
        invers = Inverion(right, invers)

        i,j,k = 0,0,0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                N[k] = left[i]
                i += 1
            else:
                N[k] = right[j]
                j = j+1
                invers += len(left)-i
            k = k+1
        while i < len(left):
            N[k] = left[i]
            i = i+1
            k = k+1
        while j < len(right):
            N[k] = right[j]
            j = j+1
            k = k+1

    return invers


invers = 0
n = int(input())
N = list(map(int, input().split()))[:n]
invers = Inverion(N, invers)
print(invers)