
def finder(num, arr):
    k = [0] * num  
    stack = [num - 1]
    k[num - 1] = -1
    for i in range(num - 2, -1, -1):
        if arr[stack[-1]] >= arr[i]:
            while (stack != []) and (arr[stack[-1]] >= arr[i]):
                stack.pop()
            if not stack:
                k[i] = -1
            else:
                k[i] = stack[-1]
            stack.append(i)
        else:
            k[i] = stack[-1]
            stack.append(i)
    return k
n = int(input())  
K = list(map(int, input().split()))  
K = finder(n,K)
print(' '.join(map(str, K))) 