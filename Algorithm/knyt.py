def prefix(str):
    p = [0] * len(str)
    for i in range(len(str)-1):
        j = p[i]
        while j > 0 and str[i+1] != str[j]:
            j = p[j-1]
        if str[i+1] == str[j]:
            p[i+1] = j + 1
        else: 
            p[i+1] = 0
    return p 


def main():
    str = input() # основная строка
    t = input() # побочная строка
    new_string = t + "&" + str
    p = prefix(new_string)
    for i in range(len(p)):
        if p[i] == len(t):
            print(i - 2 * len(t), end = " ")
            
main()