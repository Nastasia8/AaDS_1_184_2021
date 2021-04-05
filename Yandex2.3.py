def merge(mas, lst):
    new_lst = [] 
    i, j = 0, 0
    while i < len(mas) and j < len(lst):
        if mas[i] < lst[j]:
            new_lst.append(mas[i])
            i += 1
        else:
            new_lst.append(lst[j])
            j += 1
    while i < len(mas):   
        new_lst.append(mas[i])
        i += 1
    while j < len(lst):
        new_lst.append(lst[j])
        j += 1

    return new_lst 

def mergeSort(mas, indx):
    if len(mas) < 2:
        return mas
    else:
        mid = len(mas)//2
        left = mergeSort(mas[:mid], [indx[0],indx[0]+mid])
        right = mergeSort(mas[mid:],[indx[0]+mid, indx[1]]) 

        sort = merge(left, right)
        print(indx[0]+1, indx[1], sort[0], sort[-1])  
        return sort

n = int(input())
mas = list(map(int, input().split())) 
mas = mergeSort(mas,[0, n])
print(' '.join(map(str, mas)))
