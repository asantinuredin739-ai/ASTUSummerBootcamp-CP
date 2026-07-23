for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr2=arr[:]
    arr2.sort()
    ans=[]
    for i in arr:
        if i == arr2[-1]:
           ans.append(i-arr2[-2])
        else:
              ans.append(i-arr2[-1])
    print(*ans)
