size = int(input())
a = list(input() for _ in range(0, size))

print("Initial array:")
print(*a, sep=", ")

for i in range(len(a[0]) - 1, -1, -1):
    print("**********")
    print("Phase", len(a[0])-i)

    buckets = [[] for _ in range(10)]
    for j in range(len(a)):
        buckets[ord(a[j][i]) - ord("0")].append(a[j])

    for j in range(10):
        if len(buckets[j]) == 0:
            print("Bucket", str(j) + ": empty")
        else:
            print("Bucket", str(j) + ":", end=" ")

            for l in range(len(buckets[j]) - 1):
                print(buckets[j][l], end=', ')
            print(buckets[j][len(buckets[j]) - 1])

        r = 0
        for l in range(10):
            for k in range(len(buckets[l])):
                a[r] = buckets[l][k]
                r += 1

print("**********")
print("Sorted array:")
print(*a, sep=", ")
