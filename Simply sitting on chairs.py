t = int(input())
#ans=0
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    forward= 0

    for i in range(n):
        if p[i] <= i + 1:
            forward+= 1

    print(forward)
