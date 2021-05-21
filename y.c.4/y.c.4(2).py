quantity = int(input())
train = list(map(int, input().split()))
dead_end = [0] 
way_B = [0] 
for i in range(quantity):
    while dead_end[-1] == way_B[-1] + 1: 
        way_B.append(dead_end[-1])       
        dead_end.pop()
    if train[i] == way_B[-1] + 1:  
        way_B.append(train[i])    
    else:
        dead_end.append(train[i])
while dead_end[-1] == way_B[-1] + 1: 
    way_B.append(dead_end[-1])       
    dead_end.pop() 
if way_B[-1] == quantity: 
    print('YES')  
else:
    print('NO')