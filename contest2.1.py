x = input()
array = input()
sl = array.split(" ")
result = []
for i in sl:
    result.append(int(i))
x = len(result)
a = 0
for i in range(0, x-1):
    for j in range(0, x-1-i):
        if result[j] > result[j+1]:
            result[j], result[j+1] = result[j+1], result[j]
            a+=1
            print(" ".join(map(str, result)))
if a == 0:
    print(0) 