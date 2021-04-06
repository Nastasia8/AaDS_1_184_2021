a = []
length = int(input())
r = 10
Phase = 0
for i in range(length):
    a.append(input())
print("Initial array:")
print(', '.join(a))
count = len(a[0])
for i in range(count - 1, -1, -1):
    Phase += 1
    print('**********')
    print(f'Phase {Phase}')
    bucket = [[] for _ in range(r)]
    for j in range(len(a)):
        bucket[ord(a[j][i]) - ord('0')].append(a[j])
    for j in range(r):
        if len(bucket[j]) == 0:
            print(f'Bucket {j}: empty')
        else:
            print("Bucket " + str(j) + ": ", end='')
            for now in range(len(bucket[j]) - 1):
                print(bucket[j][now], end=', ')
            print(bucket[j][len(bucket[j]) - 1])
    p = 0
    for j in range(r):
        for k in range(len(bucket[j])):
            a[p] = bucket[j][k]
            p += 1
print('**********')
print("Sorted array:")
print(', '.join(a))