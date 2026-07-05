t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    left=0
    right=n-1
    for i in range(1,n):
        if i == arr[left]:
            left+=1
        elif i ==arr[right]:
            right-=1
        else:
            print("NO")
            break
    else:
        print("YES")
