from collections import deque

first_stack = deque(list(map(int, input().split())))
second_stack = deque(list(map(int, input().split())))

count = 0

while  (count < 1e6) and (len(first_stack)*len(second_stack)):
    first_motion = first_stack.popleft()
    second_motion = second_stack.popleft()

    if (first_motion == 0) and (second_motion == 9):
        first_stack.append(first_motion)
        first_stack.append(second_motion)
        count += 1
    elif (first_motion == 9) and (second_motion == 0):
        second_stack.append(first_motion)
        second_stack.append(second_motion)
        count += 1
    elif first_motion > second_motion:
        first_stack.append(first_motion)
        first_stack.append(second_motion)
        count += 1
    else:
        second_stack.append(first_motion)
        second_stack.append(second_motion)
        count += 1
    
if not first_stack:
    print(f'second {count}')
elif not second_stack:
    print(f'first {count}')
else:
    print('botva')
    