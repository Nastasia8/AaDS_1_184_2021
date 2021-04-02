a = int(input())     
s = list(map(int,input().split(maxsplit=a)))   
b = int(input()) 
k = list(map(int,input().split(maxsplit=b)))                                       
for i in range(0, b):                                        
    s[(k[i]) - 1] = s[(k[i])-1] - 1         
for i in s:                                                  
    if i < 0:                                           
        print('yes')                                            
    else:                                                       
        print('no')                               
                     
