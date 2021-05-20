a = int(input())
train = list(map(int, input().split()))
end = [0]
b = [0]
for i in range(a):
    while end[-1] == b[-1] + 1: 
        b.append(end[-1])        
        end.pop()
    if train[i] == b[-1] + 1: 
        b.append(train[i])     
    else:
        end.append(train[i])
while end[-1] == b[-1] + 1: 
    b.append(end[-1])       
    end.pop() 
if b[-1] == a: 
    print('yes')  
else:
    print('no')