
n = int(input())                                                
c = list(map(int,input().split(maxsplit=n)))                                       
k = int(input())                                                
p = list(map(int,input().split(maxsplit=k)))                                       
for i in range(0, k):                                        
    c[(p[i]) - 1] = c[(p[i])-1] - 1         
for i in c:                                                  
    if i <0:                                           
        print('yes')                                            
    else:                                                       
        print('no')   