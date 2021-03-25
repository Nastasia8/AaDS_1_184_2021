x = input("kol-vo chisel: ")
array = input("chisla: " )
b = array.split(" ")
result = []
for i in b:
    result.append(int(i))
x = len(result)
s = 0
for i in range(0, x-1):
    for j in range(0, x-1-i):
        if result[j] > result[j+1]:
            result[j], result[j+1] = result[j+1], result[j]
            s+=1
            print(" ".join(map(str, result)))
if s == 0:
    print(0) 