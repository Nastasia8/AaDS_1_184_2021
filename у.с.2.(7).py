Array = []
length = int(input())
for i in range(length):
    Array.append(input())
print("Initial array:")
print(', '.join(Array))
Count = len(Array[0])
Phase=0
Rang=10
for i in range(Count-1,-1,-1):
    Phase+=1
    print('**********')
    print(f'Phase {Phase}')
    bucket = [[] for _ in range(Rang)]
    for j in range(len(Array)):
        bucket[ord(Array[j][i]) - ord('0')].append(Array[j])
    for j in range(Rang):
        if len(bucket[j])==0:
            print(f'Bucket {j}: empty')
        else:
            print("Bucket "+str(j)+": ", end='')
            for now in range(len(bucket[j])-1):
                print(bucket[j][now],end=', ')
            print(bucket[j][len(bucket[j])-1])
    p = 0
    for j in range(Rang):
        for k in range(len(bucket[j])):
          Array[p] = bucket[j][k]
          p += 1
 
print('**********')
print("Sorted array:")
print(', '.join(Array))