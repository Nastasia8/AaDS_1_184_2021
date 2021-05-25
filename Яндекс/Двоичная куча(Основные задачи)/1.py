def shift_up(ind, heap):
    while heap[ind] > heap[(ind-1)//2] and (ind-1)//2 >= 0:
        heap[ind], heap[(ind-1)//2] = heap[(ind-1)//2], heap[ind]
        ind = (ind-1)//2
    return ind+1

def shift_down(ind, heap):
    while 2*ind+1 < len(heap):
        left_index = 2*ind+1
        right_index = 2*ind+2
        in_ind = left_index
        if right_index < len(heap) and heap[left_index] < heap[right_index]:
            in_ind = right_index
        if heap[in_ind] <= heap[ind]:
            break
        heap[ind], heap[in_ind] = heap[in_ind], heap[ind]
        ind = in_ind
    return ind+1

def add(i, heap): #+добавляем
    heap.append(i)
    return shift_up(len(heap)-1, heap)

    
def extract(heap): #-извлекаем
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    ind = heap.pop()
    if heap:
        return shift_down(0, heap), ind
    else:
        return 0, ind

def get_max(heap):
    return heap[0]

def main():
    heap = []
    res = []
    i = input().split()
    n, m = int(i[0]), int(i[1])
    for i in range(m):
        data = input().split()
        if int(data[0]) == 1:
            if not heap: #если нельзя добавить эл-т...
                res.append(-1)
            else:
                res.append(extract(heap))
        elif int(data[0]) == 2:
            if len(heap) == n:
                res.append(-1)
            else:
                res.append(add(int(data[-1]), heap))
    for i in res:
        if type(i) == tuple:
            print(*i)
        else:
            print(i)
    print(*heap)

main()