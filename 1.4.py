import math
def calc(p, m, n):
    return p*math.pow((1+(15/100/(m/12))), m/(12*n))
p = int(input("P ="))
m = int(input("m ="))
n = int(input("n ="))
print(calc(p, m, n))