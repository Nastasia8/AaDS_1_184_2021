def Func(list_, symbol):
    max_len = 0
    for i in range(0, len(list_)):
        if  len(list_[i]) > max_len:
            max_len = len(list_[i])

    for i in range(0, len(list_)):
        while(len(list_[i]) < max_len):
            list_[i] += symbol

first_list = ['Bass', 'Roach', 'Catfish', 'Trout', 'Mackerel',  'Anchovy']
second_list = ['Clematis', 'Dahlia', 'Rose', 'Chrysanthemum', 'Freesia', 'Lily', 'Peony']   

Func(first_list, '&')
print(first_list)
print()

Func(second_list, '*')
print(second_list)



