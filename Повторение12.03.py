def funct(n,tup):
    if n in tup:
        start = tup.index(n)
        c = tup.count(n)
        if c == 1:
            return tup[start:]
         else:
            i = 1
            end = start
            while i<c:
                end = tup.index(n, end + 1)
                i+=1
            return tup[start: end+1]
            #return tup[start:len(tup)-tup[::-1].index(n)]
    else:
        return "The tuple doesn't contain a character" + n
    pass
tup = (1, 2, 3, 4, 5, 4, 6, 2, 4, 7, 9, 4, 5, 6, 5, 0, 4, 2)
a = int(input("Введите число: "))
print(funct(a,tup))