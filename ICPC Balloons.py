t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    ballon=0
    y=[]
    for i in range(len(s)):
        if s[i] not in y:
            ballon+=2
            y.append(s[i])
        else:
            ballon+=1
            y.append(s[i])
    print(ballon)
