n = int(input())
a = list(map(int, input().split()))[:n]

def main():
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                isSorted = False
        print(*a)

if a == sorted(a):
  print(0)
else:
  main()
