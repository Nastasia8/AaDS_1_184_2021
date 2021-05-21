# Решение не проходит 1 тест (ошибка во время исполнения), хотя код вроде работает

size = int(input())
a = list(int(i) for i in input().split(" "))[:size]
last_elements = {a[len(a) - 1] : len(a) - 1}
output = [-1]

for i in reversed(range(0, len(a) - 1)):
    if a[i] == min(last_elements):
        last_elements.update({a[i] : i})
        output.append(-1)
    else:
        for j in reversed(last_elements.keys()):
            if j < a[i]:
                output.append(last_elements[j])
                break
        last_elements.update({a[i] : i})

print(*reversed(output))
