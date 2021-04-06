from collections import deque

number = int(input())

q_1 = deque()
q_2 = deque()
q_3 = deque()
q_4 = deque()

for item in range(number):
    num, surname = map(str, input().split())

    if int(num) == 1:
        q_1.append(surname)
    elif int(num) == 2:
        q_2.append(surname)
    elif int(num) == 3:
        q_3.append(surname)
    elif int(num) == 4:
        q_4.append(surname)

while q_1:
    print(1, q_1.popleft())
while q_2:
    print(2, q_2.popleft())
while q_3:
    print(3, q_3.popleft())
while q_4:
    print(4, q_4.popleft())
