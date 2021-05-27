final_sort = []
x = int(input())
s = input()
n = s.split()
for i in n:
    final_sort.append(int(i))
print(len(set(final_sort)))