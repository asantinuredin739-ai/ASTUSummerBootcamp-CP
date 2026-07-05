t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    mx = 0
    cur = 0
    for c in s:
        if c == '1':
            cur += 1
            mx = max(mx, cur)
        else:
            cur = 0

    if mx >= k:
        print("NO")
        continue

    print("YES")

    ans = [0] * n
    big = n
    small = 1

    for i in range(n):
        if s[i] == '0':
            ans[i] = big
            big -= 1

    for i in range(n):
        if s[i] == '1':
            ans[i] = small
            small += 1

    print(*ans)
