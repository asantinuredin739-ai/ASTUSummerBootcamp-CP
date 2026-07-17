t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=[]
    pre=0
    for i in range(n):
        pre+=a[i]
        if(i==0):
            ans.append(a[i])
        else:
            an=min(ans[i-1],pre//(i+1))
            ans.append(an)
    print(*(ans))
