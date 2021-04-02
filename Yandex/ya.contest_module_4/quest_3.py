num = int(input())

list_ = list(map(int,input().split()))

stack = [0]*num

for i in range(num - 1):
    for j in range(1, num):
        if list_[i] > list_[j]:
            stack[i] = j
            break
    n += 1
for i in range(0, length):
    if (stack[i] == 0):
        stack[i] = -1

print(' '.join(map(str, stack)))

# in process