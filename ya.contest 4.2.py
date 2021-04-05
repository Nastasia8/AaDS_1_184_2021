leng = int(input())
lst1 = list(map(int,input().split()))
lst2 = []
stack = []
test =  sorted(lst1)
for i in range(leng):
    if (stack == []) or (stack[-1] > lst1[0]):
        stack.append(lst1[0])
        lst1.pop(0)
    else:
        while (stack != [] and stack[-1] < lst1[0]):
            lst2.append(stack[-1])
            stack.pop(-1)
        if (stack == []) or (stack[-1] > lst1[0]):
            stack.append(lst1[0])
            lst1.pop(0)        
if stack != []: 
    for i in range(len(stack)):
        lst2.append(stack[-1])
        stack.pop(-1)   
if lst2 == test:
    print("yes")
else: 
    print("no") 
