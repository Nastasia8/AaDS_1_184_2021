def min(j, window, arr):
    stack = []
    for i in range(window):
        while stack != [] and arr[i] <= arr[stack[-1]]:
            stack.pop()
        stack.append(i)
    for i in range(window, j):
        print(arr[stack[0]])
        while stack != [] and i - window >= stack[0]:
            stack.pop(0)
        while stack != [] and arr[i] <= arr[stack[-1]]:
            stack.pop()
        stack.append(i)
    print(arr[stack[0]])


j, window = map(int, input().split())
arr = list(map(int, input().split()))
min(j, window, arr)