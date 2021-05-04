def prefix(s):
    p = [0]*len(s)
    for i in range(len(s)-1):
        j = p[i]
        while j>0 and s[i+1]!=s[j]:
            j = p[j-1]
        if s[i+1]==s[j]:
            p[i+1]=j+1
        else:
            p[i+1]=0
    return p
def main():
    s = input()
    # l = len(s)
    pref = prefix(s)
    if (len(s) % (len(s) - pref[-1]) == 0):
        print(len(s) // (len(s) - pref[-1]))
    else:
        print("1")
main()
