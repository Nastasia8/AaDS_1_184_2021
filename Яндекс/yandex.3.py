n = int(input())
M= list(int(i) for i in input().split(" "))

def merge_sort(M):
    if len(M)>1:
        mid=len(M)//2
        right=M[mid:]
        left=M[:mid]

        merge_sort(right)
        merge_sort(left)
        print(' '.join(map(str, M)))
        i, j, k=0,0,0
        while i<len(right) and j<len(left):
            if left[j]>right[i]:
                M[k]=right[i]
                i+=1
            else:
                M[k]= left[j]
                j+=1
            k+=1

        while i <len(right):
            M[k]=right[i]
            i+=1
            k+=1
        while j <len(left):
            M[k]=left[j]
            j+=1
            k+=1

    return M


M=merge_sort(M)
print(' '.join(map(str, M)))
# проблема с правильным выводом