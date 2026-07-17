t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    x=list(map(int,input().split()))
    max_idx=[]
    y=max(x) 
    for _ in range(m):
        op,l,r=input().split()
        l_int=int(l)
        r_int=int(r)
        if l_int<=y<=r_int:
            if op=="+":
                y+=1
            elif op=="-":
                y-=1
        max_idx.append(y)           
    print(*max_idx)
