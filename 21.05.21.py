#1
class Heap:
    __arr = []

    @property
    def length(self):
        return len(self.__arr)

    @property
    def get_min(self):
        return self.__arr[0]

    def shift_down(self, current_indx):  # операция
        while 2 * current_indx + 1 < self.length:
            left_indx = 2 * current_indx + 1
            right_indx = 2 * current_indx + 2
            child_indx = left_indx
            if right_indx < self.length and self.__arr[left_indx] < self.__arr[right_indx]:
                child_indx = right_indx
            if self.__arr[child_indx] <= self.__arr[current_indx]:
                break
            self.__arr[current_indx], self.__arr[child_indx] = self.__arr[child_indx], self.__arr[current_indx]
            current_indx = child_indx

    def shift_up(self, current_indx):
        while current_indx > 0 and self.__arr[current_indx] > self.__arr[(current_indx - 1) // 2]:
            self.__arr[current_indx], self.__arr[(current_indx - 1) // 2] = self.__arr[(current_indx - 1) // 2], \
                                                                            self.__arr[current_indx]
            current_indx = (current_indx - 1) // 2

    def extract(self):
        self.__arr[0], self.__arr[-1] = self.__arr[-1], self.__arr[0]
        self.__arr.pop()
        self.shift_down(0)

    def add(self, value):
        self.__arr.append(value)
        self.shift_up(self.length - 1)

    def get_max(self):
        return self.__arr[0]

    def display(self):
        print(*self.__arr)

def build(arr):
    heap = arr[:]
    h = Heap(heap)
    for i in range(len(heap) - 1, -1, -1):
        h.shift_down(i)
    return h

def main():
    n = int(input())
    res = []
    heap = Heap()
    for i in range(n):
        command = list(map(int, input().split()))
        if command[0] == 0:
            heap.add(command[1])
        else:
            res.append(heap.get_max())
            heap.extract()
    print(*res, sep="\n")
main()

#2
class Heap:
    def __init__(self, arr):
        self.__arr = arr

    @property
    def length(self):
        return len(self.__arr)

    @property
    def get_min(self):
        return self.__arr[0]

    def shift_down(self, current_indx):  # операция
        while 2 * current_indx + 1 < self.length:
            left_indx = 2 * current_indx + 1
            right_indx = 2 * current_indx + 2
            child_indx = left_indx
            if right_indx < self.length and self.__arr[left_indx] > self.__arr[right_indx]:
                child_indx = right_indx
            if self.__arr[child_indx] >= self.__arr[current_indx]:
                break
            self.__arr[current_indx], self.__arr[child_indx] = self.__arr[child_indx], self.__arr[current_indx]
            current_indx = child_indx

    def shift_up(self, current_indx):
        while current_indx > 0 and self.__arr[current_indx] < self.__arr[(current_indx - 1) // 2]:
            self.__arr[current_indx], self.__arr[(current_indx - 1) // 2] = self.__arr[(current_indx - 1) // 2], \
                                                                            self.__arr[current_indx]
            current_indx = (current_indx - 1) // 2

    def extract(self):
        self.__arr[0], self.__arr[-1] = self.__arr[-1], self.__arr[0]
        self.__arr.pop()
        self.shift_down(0)

    def add(self, value):
        self.__arr.append(value)
        self.shift_up(self.len - 1)

    def get_min(self):
        return self.__arr[0]

    def display(self):
        print(*self.__arr)

def build(arr):
    heap = arr[:]
    h = Heap(heap)
    for i in range(len(heap) - 1, -1, -1):
        h.shift_down(i)
    return h

def main():
    n = int(input())
    arr = [int(i) for i in input().split(maxsplit=n)]
    heap = build(arr)

    while heap.length:
        print(heap.get_min(), end=" ")
        heap.extract()
main()

#3
class Heap:
    __arr = []

    @property
    def length(self):
        return len(self.__arr)

    @property
    def get_min(self):
        return self.__arr[0]

    @property
    def empty(self):
        return self.length == 0

    def shift_down(self, current_indx):
        while 2 * current_indx + 1 < self.length:
            left_indx = 2 * current_indx + 1
            right_indx = 2 * current_indx + 2
            child_indx = left_indx
            if right_indx < self.length and self.__arr[left_indx] < self.__arr[right_indx]:
                child_indx = right_indx
            if self.__arr[child_indx] <= self.__arr[current_indx]:
                break
            self.__arr[current_indx], self.__arr[child_indx] = self.__arr[child_indx], self.__arr[current_indx]
            current_indx = child_indx

    def shift_up(self, current_indx):
        while current_indx > 0 and self.__arr[current_indx] > self.__arr[(current_indx - 1) // 2]:
            self.__arr[current_indx], self.__arr[(current_indx - 1) // 2] = self.__arr[(current_indx - 1) // 2], \
                                                                            self.__arr[current_indx]
            current_indx = (current_indx - 1) // 2

    def clear(self):
        self.__arr.clear()

    def extract(self):
        self.__arr[0], self.__arr[-1] = self.__arr[-1], self.__arr[0]
        self.__arr.pop()
        self.shift_down(0)

    def add(self, value):
        self.__arr.append(value)
        self.shift_up(self.length - 1)

    def get_max(self):
        return self.__arr[0]

    def display(self):
        print(*self.__arr)

def build(arr):
    heap = arr[:]
    h = Heap(heap)
    for i in range(len(heap) - 1, -1, -1):
        h.shift_down(i)
    return h

def main():
    n = int(input())
    res = []
    heap = Heap()
    for i in range(n):
        command = list(map(str, input().split()))
        if command[0] == "ADD":
            heap.add(int(command[1]))
        elif command[0] == "EXTRACT":
            if heap.empty:
                res.append("CANNOT")
            else:
                res.append(heap.get_max())
                heap.extract()
        else:
            heap.clear()
    print(*res, sep="\n")
main()

