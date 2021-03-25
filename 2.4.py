num = list(range(1,26))
def funct(w):
    num[0], num[-1] = num[-1], num[0]
    return num
print(funct(words))