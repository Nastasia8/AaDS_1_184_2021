def shift_down(v, heap): 
    while 2*v+1 < len(heap):
        l_ind = 2*v+1
        r_ind = 2*v+2
        ind = 2*v+1
        if r_ind < len(heap) and heap[l_ind] < heap[r_ind]:
            ind = r_ind
        if heap[ind] <= heap[v]:
            break
        heap[v], heap[ind] = heap[ind], heap[v]
        v = ind

def extract(heap):
    heap[0], heap[-1] = heap[-1], heap[0]
    a = heap.pop()
    shift_down(0, heap)
    return a

def get_max(heap):
    return heap[0]

def build(arr):
    heap = arr[:]
    for i in range(len(heap)-1, -1, -1):
        shift_down(i, heap)
    return heap

def main():
    num = int(input())
    res = []
    numbers = list(map(int, input().split()))[:num]
    heap = build(numbers)
    for i in range(num):
        print(*heap)
        res.append(extract(heap))
    res.reverse()
    print(*res)
main()