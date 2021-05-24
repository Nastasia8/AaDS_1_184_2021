def prefix(a):
    p = [0] * len(a)
    for i in range(len(a) - 1):
        j = p[i]
        while j > 0 and a[i + 1] != a[j]:
            j = p[j - 1]
        if a[i + 1] == a[j]:
            p[i + 1] = j + 1
        else:
            p[i + 1] = 0
    return p
def main():
    x=input()
    p=prefix(x)
    print(len(x)-p[-1])
main()