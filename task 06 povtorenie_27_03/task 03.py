from collections import deque

size = int(input())
list = deque()

for i in range(size):
    list.append(input())

left = deque()
right = deque()
for line in list:
    if int(line[0]) == 1:
        left.appendleft(line)
    elif int(line[0]) == 2:
        left.append(line)
    elif int(line[0]) == 3:
        right.appendleft(line)
    elif int(line[0]) == 4:
        right.append(line)

print(left, right)
