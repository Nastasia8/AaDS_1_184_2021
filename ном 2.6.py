#6
def funcct(a,b):
    if a.intersection(b):
        print('True')
        return True
    print('False')
    return False

mn={0, 2, 7}
e=list(range(4,5))
funcct(mn,e)

# Написать функцию, принимающую два параметра: 1-ый параметр -> множество
# , 2-ой  -> список и возвращающую значение False, если хотя бы один из элементов списка не содержится в множестве,
# иначе возвращающая True.


