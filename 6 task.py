n = int(input())                                                
a = list(map(int,input().split(maxsplit=n)))                                       
k = int(input())                                                
p = list(map(int,input().split(maxsplit=k)))                                       
for i in range(0, k):                                        
    a[(p[i]) - 1] = a[(p[i])-1] - 1         
for i in a:                                                  
    if i <0:                                           
        print('yes')                                            
    else:                                                       
        print('no')   
