n = []
S = int(input())
for j in range(S):
    b  = input().split()
    for j in range(len(b)):
        b[j] = int(b[j])
    n.append(b)
for j in range(S-1):
    for i in range(S-j-1):
      if  (n[i][1]<n[i+1][1]):
        n[i],n[i+1]=n[i+1],n[i]
      elif ( (n[i][0] > n[i+1][0]) and (n[i][1] == n[i+1][1])):
        n[i],n[i+1]=n[i+1],n[i]
for j in range(S):
    print(n[j][0],n[j][1])
    