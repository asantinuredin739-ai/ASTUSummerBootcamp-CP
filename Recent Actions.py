t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))

    ans = [-1] * n
    seen = set()

    pos = n - 1

    for i in range(m):
        if p[i] not in seen:
            seen.add(p[i])
            if pos >= 0:
                ans[pos] = i + 1
                pos -= 1

    print(*ans)
