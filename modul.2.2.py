n = int(input())
pairs = []  
for i in range(0, n):  
    _str = input()  
    _split = _str.split(' ')  
    pair = (int(_split[0])), int(_split[1])  
    pairs.append(pair) 
 
pairs.sort(key=(lambda x: x[0])) 

pairs.sort(key=lambda x: x[1], reverse=True)  
for i in pairs:  
    print(str(i[0]) + " " + str(i[1]))
