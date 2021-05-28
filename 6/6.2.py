def shift_up(index, heap):
    while heap[index] > heap[(index-1) // 2] and (index-1) // 2 >= 0:
        heap[index], heap[(index-1) // 2] = heap[(index-1) // 2], heap[index]
        index = (index-1) // 2
    return index + 1

def shift_down(index, heap):
    while 2 * index + 1 < len(heap):
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        child_index = left_index

        if right_index < len(heap) and heap[left_index] < heap[right_index]:
            child_index = right_index

        if heap[child_index] <= heap[index]:
            break

        heap[index], heap[child_index] = heap[child_index], heap[index]
        index = child_index
    return index + 1


def get_max(heap):
    return heap[0]


def add(i, heap):
    heap.append(i)
    return shift_up(len(heap)-1, heap)


def extract(heap):
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    index = heap.pop()
    if heap:
        return shift_down(0, heap), index
    else:
        return 0, index


def direct_extract(index, heap):
    val = heap[len(heap)-1]
    heap[index-1], heap[len(heap)-1] = heap[len(heap)-1], heap[index-1]
    i = heap.pop()
    if val < i:
        shift_down(index-1, heap)
    elif val > i:
        shift_up(index-1, heap)
    return i

heap = []
result = []
num = input().split()
t1, t2 = int(num[0]), int(num[1])

for _ in range(t2):
    data = input().split()
    if int(data[0]) == 1:
        if heap == []:
            result.append(-1)
        else:
            result.append(extract(heap))

    elif int(data[0]) == 2:
        if len(heap) == t1:
            result.append(-1)
        else:
            result.append(add(int(data[-1]), heap))

    elif int(data[0]) == 3:
        if len(heap) >= int(data[-1]) > 0:
            result.append(direct_extract(int(data[-1]), heap))
        else:
            result.append(-1)

for item in result:
    if type(item) == tuple:
        print(*item)
    else:
        print(item)

print(*heap)
