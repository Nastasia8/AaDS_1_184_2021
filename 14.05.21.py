def shift_up(v, heap):
    while heap[v] < heap[(v-1)//2]:  # на > для кучи по максимуму
        heap[v], heap[(v-1)//2] = heap[(v-1)//2], heap[v]
        v = (v-1)//2
def shift_down(v, heap):
    while 2*v+1 < len(heap):
        left_indx = 2*v + 1
        right_indx = 2*v + 2
        _indx = 2*v+1
        if right_indx < len(heap) and heap[left_indx] > heap[right_indx]: # второе условие < для кучи по макс
            _indx = right_indx
        if heap[_indx] >= heap[v]: # <=
            break
        heap[v], heap[_indx] = heap[_indx], heap[v]
        v = _indx
def delete(heap):
    heap[0], heap[-1] = heap[-1], heap[0]
    heap.pop()
    shift_down(0, heap)
def add(value, heap):
    heap.append(value)
    shift_up(len(heap)-1, heap)
def get_min(heap):
    return heap[0]
def build(arr):
    heap = arr[:]
    for i in range(len(heap)-1, -1, -1):
        shift_down(i, heap)
    return heap
def main():
    n=int(input())
    arr = list(map(str, input().split()))[:n]
    heap = build(arr)
    print(*heap)
    while len(heap):
        print(get_min(heap), end=" ")
        delete(heap)
main()

#5
#5 1 2 8 9
