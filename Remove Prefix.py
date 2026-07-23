t=int(input())
for _ in range(t):
    n=int(input())
    x=list(map(int,input().split()))
    y=set()
    count=0
    for i in range(len(x)-1,-1,-1):
        if x[i]  not in (y):
           y.add(x[i])
        else:
            count=i+1
            break
           
    print(count)
