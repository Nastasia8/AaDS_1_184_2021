a = list(i for i in input())

rightCount = 0
leftCount = 0

for i in a:
    if i == "(":
        rightCount += 1
    elif i == ")":
        if rightCount >= 1:
            rightCount -= 1
        else:
            leftCount += 1

print(rightCount + leftCount)
