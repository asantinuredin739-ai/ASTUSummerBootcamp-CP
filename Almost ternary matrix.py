t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    for i in range(n):
        row = []
        for j in range(m):
            if ((i // 2) + (j // 2)) % 2 == 0:
                if i % 2 == 0:
                    row.append(1 if j % 2 == 0 else 0)
                else:
                    row.append(0 if j % 2 == 0 else 1)
            else:
                if i % 2 == 0:
                    row.append(0 if j % 2 == 0 else 1)
                else:
                    row.append(1 if j % 2 == 0 else 0)
        print(*row)
