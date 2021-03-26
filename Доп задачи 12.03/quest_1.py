def function(tuple_, symbol):
    if symbol in tuple_:
        start = tuple_.index(symbol)
        k = tuple_.count(symbol)
        if k == 1:
            return tuple_[start:]
        else:
            i = 1
            end = start
            while i < k:
                end = tuple_.index(symbol, end + 1)
                i += 1
            return tuple_[start: end + 1 ]



tuple =  (1, 2, 3, 4, 5, 4, 6, 2, 4, 7, 9, 4, 5, 6, 5, 0, 4, 2) 
print(function(tuple, 5))