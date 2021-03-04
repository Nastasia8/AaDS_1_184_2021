def funct(list_,symb):
    max_len=0
    for i in range(0, len(list_)):
        if len(list_[i])> max_len:
            max_len =len(list_[i])
    print('max_len =',max_len)

    for i in range(0, len(list_)):
        while(len(list_[i]))< max_len:
            list_[i]+=symb


frst_list=[ 'Bass', 'Roach', 'Catfish', 'Trout', 'Mackerel',  'Anchovy']
scnd_list=['Clematis', 'Dahlia', 'Rose', 'Chrysanthemum', 'Freesia', 'Lily', 'Peony']
funct(frst_list,'$')
print(frst_list)
print()
funct(scnd_list,'$')
print(scnd_list)
