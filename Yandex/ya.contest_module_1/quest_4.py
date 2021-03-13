def inversion(inversion, n):    
    inv_count = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            if array[i] > array[j]:
                inv_count += 1
    return inv_count

n = int(input())

array = list(map(int, input().split()))
print(inversion(array, n))
