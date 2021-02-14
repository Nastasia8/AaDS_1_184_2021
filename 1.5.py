import math
def calc(k):
    answer = 1
    for n in range(k):
        answer = answer * ((n+math.pow(3, n))/(n+math.pow(5, 2*n)))
    return answer
k = int(input("K = "))
print("Answer = ", calc(k))