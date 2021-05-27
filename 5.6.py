def build(value, left, right, segments_tree, numbers): #строим дерево
    if right - left == 1:
        segments_tree[value] = numbers[left]
        return

    middle = (right + left) // 2

    build(2 * value + 1, left, middle, segments_tree, numbers)
    build(2 * value + 2, middle, right, segments_tree, numbers)

    segments_tree[value] = segments_tree[2 * value + 1] + segments_tree[2 * value + 2]

def get_k_zero(value, left, right, segments_tree, number): # ищем k ноль
    if number > segments_tree[value]:
        return -1
    if right - left == 1:
        return right

    middle = (right + left) // 2

    if segments_tree[2 * value + 1] >= number:
        return get_k_zero(2 * value + 1, left, middle, segments_tree, number)
    else:
        return get_k_zero(2 * value + 2, middle, right, segments_tree, number - segments_tree[2 * value + 1])

def get_sum(value, left, right, segments_tree, q_left, q_right): # ищем сумму
    if q_left <= left and q_right >= right:
        return segments_tree[value]

    if q_left >= right or q_right <= left:
        return 0

    middle = (right + left) // 2

    t_left = get_sum(2 * value + 1, left, middle, segments_tree, q_left, q_right)
    t_right = get_sum(2 * value + 2, middle, right, segments_tree, q_left, q_right)

    return t_left + t_right

def update(value, left, right, segments_tree, index, number):# добавление функции для динамического дерева 
    if right - left == 1:
        segments_tree[value] = number
        return

    middle = (right + left) // 2
    if index < middle:
        update(2 * value + 1, left, middle, segments_tree, index, number)
    else:
        update(2 * value + 2, middle, right, segments_tree, index, number)
    segments_tree[value] = segments_tree[2 * value + 1] + segments_tree[2 * value + 2]

n = int(input())
numbers = [0 if int(i) != 0 else 1 for i in input().split()] #  создаем лист для следующей работы
segments_tree = [0] * 4 * n
build(0, 0, n, segments_tree, numbers)
q = int(input())

res = []
while q != 0:
    item = input().split()#добавление элемента
    if len(item) == 4: # проверяем на 4
        left, right, number = int(item[1]), int(item[2]), int(item[3])#входные данные
        sum = get_sum(0, 0, n, segments_tree, left-1, right)#получаем сумму
        if sum >= number and left > 1: # если сумма > number и left > 1 -> добаляем в результат k_zero + сумма
            res.append(get_k_zero(0, 0, n, segments_tree, number + get_sum(0, 0, n, segments_tree, 0, left - 1)))
        elif sum >= number and left == 1: # если сумма > number и left == 1 -> добаляем в результат k_zero
            res.append(get_k_zero(0, 0, n, segments_tree, number))
        else: # иначе добавляем -1
            res.append(-1)
    else:
        first, second = int(item[1]), int(item[2])
        if second == 0: # если second_data == 0 -> update() - number = 0
            update(0, 0, n, segments_tree, first-1, 1)
        else:# иначе -> update() - number = 1
            update(0, 0, n, segments_tree, first-1, 0)
    q -= 1

print(*res) # выводим, * обозначает, что объектов может быть несколько

#``````````{\
#````````{\{*\
#````````{*\~\__&&&
#```````{```\`&&&&&&.
#``````{~`*`\((((((^^^)
#`````{`*`~((((((( ♛ ♛
#````{`*`~`)))))))). _' )
#````{*```*`((((((('\ ~
#`````{~`*``*)))))`.&
#``````{.*~``*((((`\`\)) ?
#````````{``~* ))) `\_.-'``
#``````````{.__ ((`-*.*
#````````````.*```~``*.
#``````````.*.``*```~`*.
#`````````.*````.````.`*.
#```````.*``~`````*````*.
#``````.*``````*`````~``*.
#````.*````~``````.`````*.
#```.*```*```.``~```*``~ *.¤´҉  фея
