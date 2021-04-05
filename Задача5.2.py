n=int(input())
a= list(map(int,input().split(maxsplit=n)))
uni = []
uni=[uni.append(i)for i in a if i not in uni]
print(len(uni))
#помогите не проходит по времени......