t=int(input())
for _ in range(t):
    n=int(input())
    x=list(map(int,input().split()))
    x.sort()
    y=set()
    z=[]
    a=[]
    for i in range(len(x)):
        if x[i] not in y:
            z.append(x[i])
            y.add(x[i])
        else:
            a.append(x[i])
    print(*(z+a))
