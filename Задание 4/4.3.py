#3
#1 доделать
n= int(input())
array= input()
str_list=array.split(" ")
res=[]
for i in str_list:
    res.append(int(i))
print(res)



def funct(list):
    list.sort()
    n_list=set(list)
    return n_list

print(funct(res))

#2

a = list(int(i) for i in input("enter list: ").split(" "))
b = []
for i in a:
    if i not in b:
        b.append(i)

b.sort()
print(tuple(b))