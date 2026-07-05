t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    bad = []

    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            bad.append(i)

    if not bad:
        print("Yes")
    elif bad[-1] - bad[0] + 1 == len(bad):
        print("Yes")
    else:
        print("No")
