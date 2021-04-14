def compare(a, b):
    if a[1] > b[1]:
        return True
    elif a[1] == b[1]:
        return a[0] > b[0]
    else:
        return False

def sort(f):
    for i in range(1, len(f)):
        tmp = f[i]
        j = i - 1
        while j >= 0 and compare(tmp, f[j]):
            f[j + 1] = f[j]
            j -= 1
        f[j + 1] = tmp

f = [[1,3], [2,7], [2,3], [4,4]]
sort(f)
print(f)