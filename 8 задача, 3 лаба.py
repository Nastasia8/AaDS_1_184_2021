def funct (array):
    for arr in array:
        for j in range (len (arr)//2):
            arr [j], arr [-j-1]=arr[-j-1],arr [j]
    return array
funct(array)