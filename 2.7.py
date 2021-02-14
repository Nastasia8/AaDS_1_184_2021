numbers = [5, 1, 3, 5, 3, 1, 0, 9, 5, 3, 8, 6, 5, 7]
answer = []
i = 0
for number in numbers:
    if number == 5:
        answer.append(i)
    i = i + 1
print(answer)