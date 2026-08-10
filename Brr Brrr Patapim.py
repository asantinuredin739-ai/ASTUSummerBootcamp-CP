t = int(input())
for _ in range(t):
    n = int(input())
    p = [0] * (2 * n + 1)
    used = set()
    for i in range(1, n + 1):
        row = list(map(int, input().split()))
        for j in range(1, n + 1):
            p[i + j] = row[j - 1]
            used.add(row[j - 1])
    for x in range(1, 2 * n + 1):
        if x not in used:
            p[1] = x
            break

    print(*p[1:])
