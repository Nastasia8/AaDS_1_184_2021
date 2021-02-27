array = [[7, 5, 9], [0, 1, 2,], [4, 7, 2]]

#for i in number:
#    for j in i[::-1]:
#       print(number[i][j])
#   print()

def funct(number):
    for arr in array:
        for j in range(len(arr)//2):
            arr[j],arr[-j-1]=arr[-j-1],arr[j]
        return array


print(funct(array))



