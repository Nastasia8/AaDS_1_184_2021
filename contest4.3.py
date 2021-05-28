def finder(num, arr):
    b = [0] * num  
    stack = [num - 1]
    b[num - 1] = -1
    for i in range(num - 2, -1, -1):
        if arr[stack[-1]] >= arr[i]:
            while (stack != []) and (arr[stack[-1]] >= arr[i]):
                stack.pop()
            if not stack:
                b[i] = -1
            else:
                b[i] = stack[-1]
            stack.append(i)
        else:
            b[i] = stack[-1]
            stack.append(i)
    return b
n = int(input())  
K = list(map(int, input().split()))  
K = finder(n,K)
print(' '.join(map(str, K))) 