

def merge_sort(M,start, end):
    if len(M)>1:
        mid=len(M)//2
        left=M[:mid]
        right=M[mid:]
      

        merge_sort(left, start, start+mid-1)
        merge_sort(right, start+mid, end)
    
        i, j, k=0,0,0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                M[k]=left[i]
                i+=1
            else:
                M[k]= right[j]
                j+=1
            k+=1

        while j <len(right):
            M[k]=right[j]
            j+=1
            k+=1
        while i <len(left):
            M[k]=left[i]
            i+=1
            k+=1
        print(start, end, M[0], M[-1])
    return M

n = int(input())
M= list(map(int, input().split()))[:n]
merge_sort(M,1,len(M))
print(*M)
