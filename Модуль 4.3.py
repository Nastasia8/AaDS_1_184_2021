def finder(num, arr):
    a = [0] * num  
    stack = [num - 1]
    a[num - 1] = -1
    for i in range(num - 2, -1, -1):
        if arr[stack[-1]] >= arr[i]:
            while (stack != []) and (arr[stack[-1]] >= arr[i]):
                stack.pop()
            if not stack:
                a[i] = -1
            else:
                a[i] = stack[-1]
            stack.append(i)
        else:
            a[i] = stack[-1]
            stack.append(i)
    return a


n = int(input())  
A = list(map(int, input().split()))  
A = finder(n,A)
print(' '.join(map(str, A)))
