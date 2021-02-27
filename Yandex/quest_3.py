n = int(input())
res = []

for i in range(n):
    number = list(map(int, input().split(' ')))
    res.append([number])

count = 0
for i in range(n-1):
    if res[i]!=res[i+1]:
        count+=1
print(count)

# in process