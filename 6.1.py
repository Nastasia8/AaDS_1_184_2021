def shift_down(index, heap): #ищем индекм левый приоритетный
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

def shift_up(index, heap):#функция поднятия индексов элементов в куче
    while heap[index] > heap[(index-1) // 2] and (index-1) // 2 >= 0:
        heap[index], heap[(index-1) // 2] = heap[(index-1) // 2], heap[index]
        index = (index-1) // 2
    return index + 1

def get_max(heap):#получаем максимум кучи
    return heap[0]

def add(item, heap):#добавление элементов
    heap.append(item)
    return shift_up(len(heap)-1, heap)


def extract(heap): #извлечение из кучи
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    index = heap.pop()
    if heap:
        return shift_down(0, heap), index
    else:
        return 0, index
heap = []
res = []
number = input().split()
first, second = int(number[0]), int(number[1])
for _ in range(second):
    data = input().split()
    if int(data[0]) == 1:
        if not heap:
            res.append(-1)
        else:
            res.append(extract(heap))

    elif int(data[0]) == 2:
        if len(heap) == first:
            res.append(-1)
        else:
            res.append(add(int(data[-1]), heap))

for item in res:
    if type(item) == tuple:
        print(*item)
    else:
        print(item)
print(*heap) # выводим, * обозначает, что объектов может быть несколько