t = int(input())

for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    
    left = 1
    right = n - 1
    
    sum_blue= x[0] + x[1]
    sum_red = x[right]
    
    possible = False
    
    while left < right:
        if sum_red > sum_blue:
            possible = True
            break
            
        left += 1
        right -= 1
        
        if left < right:
            sum_blue += x[left]
            sum_red += x[right]

    if possible:
        print("YES")
    else:
        print("NO")
