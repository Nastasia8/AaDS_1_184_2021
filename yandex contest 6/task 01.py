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
        print(current_indx + 1, end=" ")

    def shift_up(self, current_indx):
        while current_indx > 0 and self.__arr[current_indx] > self.__arr[(current_indx - 1) // 2]:
            self.__arr[current_indx], self.__arr[(current_indx - 1) // 2] = self.__arr[(current_indx - 1) // 2], \
                                                                            self.__arr[current_indx]
            current_indx = (current_indx - 1) // 2
        print(current_indx + 1)

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

inp = list(map(int, input().split()))
queue = inp[0]
n = inp[1]

heap = Heap()
for i in range(n):
    command = list(map(str, input().split()))
    if command[0] == "1":
        if heap.empty:
            print("-1")
        else:
            temp = heap.get_max()
            heap.extract()
            print(temp)
    elif command[0] == "2":
        if queue > 0:
            heap.add(int(command[1]))
            queue -= 1
        else:
            print("-1")
    else:
        heap.clear()

heap.display()
