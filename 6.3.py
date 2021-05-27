from collections import deque
class Heap:
    #инициализация объекта
    def __init__(self, arr):
        self.__heap = arr

    @property # декоратор для передачи одной функции другим функциям
    def length(self):
        return len(self.__heap)
#будем опускать элемент
    def shift_down(self, index):
        while 2*index+1 < self.length:
            left_index = 2*index+1
            right_index = 2*index+2
            child_index = left_index
            if right_index < self.length and self.__heap[left_index] < self.__heap[right_index]:
                child_index = right_index
            if self.__heap[child_index] <= self.__heap[index]:
                break
            self.__heap[index], self.__heap[child_index] = self.__heap[child_index], self.__heap[index]
            index = child_index
#будем извлекать элемент
    def extract(self):
        self.__heap[0], self.__heap[self.length-1] = self.__heap[self.length-1], self.__heap[0]
        max_ = self.__heap.pop()
        self.shift_down(0)
        return max_
#функция вывода
    def print_(self):
        print(*self.__heap)
#будем строить кучу
def build(arr):
    heap = arr[:]
    h = Heap(heap)
    for i in range(len(heap)-1, -1, -1):
        h.shift_down(i)
    return h
# ввод всякого и вывод
def main():
    n = int(input())
    list_ = list(map(int, input().split()))
    heap = build(list_)
    result = deque()
    while heap.length:
        heap.print_()
        result.appendleft(heap.extract())
    print(*result)

main()