from collections import deque
n= int(input())
q1=deque()
q2=deque()
q3=deque()
q4=deque()
for i in range(n):
    num, surname = map(str,input().split())
    if int(num)==1:
        q1.append(surname)
    elif int(num)==1:
        q1.append(surname)
    elif int(num)==1:
        q1.append(surname)  
    else:
        q4.append(surname)

while q1:
    print(1, q1.popleft())
while q2:
    print(2, q1.popleft())
while q3:
    print(3, q1.popleft())
while q4:
    print(4, q1.popleft())

    #команды