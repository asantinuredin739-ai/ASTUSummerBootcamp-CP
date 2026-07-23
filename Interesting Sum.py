t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    ans=(a[n-1]-a[0])+(a[n-2]-a[1])
    print (ans)
