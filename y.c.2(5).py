size = int(input())
a = list(int(i) for i in input().split(" "))[:size]
print(len(set(a))) #просчЄт неповтор€ющихс€ во множестве чисел с помощью метода "set"