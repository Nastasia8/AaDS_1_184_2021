def main():
    n = int(input())
    a = list(map(int, input().split(maxsplit = n)))
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                isSorted = False
        print(*a)
    
if __name__ == "__main__":
    main()