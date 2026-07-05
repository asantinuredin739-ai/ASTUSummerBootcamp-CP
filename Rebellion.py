t = int(input())
for i in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    left = 0
    right = n - 1
    operations = 0
    while left < right:
        1
        if x[left] == 0:
            left += 1
            continue
        if x[right] == 1:
            right -= 1
            continue
        if left < right:
            operations += 1
            left += 1
            right -= 1
            
    print(operations)
