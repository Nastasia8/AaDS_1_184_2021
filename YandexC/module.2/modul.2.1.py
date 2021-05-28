
n = input()
array = input()
sl = array.split(" ")
result = []
for i in sl:
    result.append(int(i))
n = len(result)
k = 0
for i in range(0, n-1):
    for j in range(0, n-1-i):
        if result[j] > result[j+1]:
            result[j], result[j+1] = result[j+1], result[j]
            k+=1
            print(" ".join(map(str, result)))
if k == 0:
    print(0) 