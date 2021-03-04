size = int(input())
a = list(int(i) for i in input().split(" "))[:size]
print(len(set(a).intersection(set(a))))
