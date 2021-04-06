a = dict()
size = int(input())
for i in range(0, size):
    cin = list(int(j) for j in input().split(" "))
    if set(list(a.keys())).intersection({cin[1]}) != set():
        a[cin[1]].append(cin[0])
    else:
        a[cin[1]] = [cin[0]]

sortedDict = []
for i in range(0, len(a)):
    dictEl = a.get(list(a.keys())[i])
    sortedDict.append(list(a.keys())[i])

sortedDict.sort()

for i in reversed(sortedDict):
    dictEl = a.get(i)
    dictEl.sort()
    for j in range(0, len(dictEl)):
        print(dictEl[j], end=" ")
        print(i)
