def get_hash(string,x,p):
    hash=0
    for item in range(len(string)):
        hash=(hash*x+ord(string[item]))%p
    return hash
def get_new_hash (string,substring,p,x):
    if string==substring:
        return 0
    else:
        h_string=get_hash(string,x,p)
        h_substring=get_hash(substring,x,p)
        xt=1
        for i in range (len(string)-1):
            xt=(xt*x)%p
        for i in range(len(string)):
            if h_string==h_substring:
                return i
                break
            else:
                h_substring = (x * (h_substring - ord(substring[i]) * xt) + ord(substring[i])) % p
        if h_string!=h_substring:
            return -1
string=input()
substring=input()
x=26
p=10**9+7
print(get_new_hash(string,substring,p,x))
