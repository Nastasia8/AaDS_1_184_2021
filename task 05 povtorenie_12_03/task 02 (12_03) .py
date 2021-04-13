a = (1, 2, 3, 4, 5, 4, 6, 2, 4, 7, 9, 4, 5, 6, 5, 0, 4, 2)

def findSame(b, el):
    found = False
    count = b.count(el)
    
    if count == 0:
        print("The tuple doesn't contain a character =", el)
    
    for i in b:
        if i == el:
            if b.count(el) == count or count == 1:
                found = not found
            count -= 1
            print(i, end=" ")
        else:
            if found:
                print(i, end=" ")

findSame(a, 3)
print()
