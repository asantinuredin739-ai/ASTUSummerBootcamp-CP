n, m = map(int, input().split())
a = list(map(int, input().split()))
right = [0] * n
for i in range(1, n):
    right[i] = right[i-1] + max(0, a[i-1] - a[i])
left = [0] * n
for i in range(n-2, -1, -1):
    left[i] = left[i+1] + max(0, a[i+1] - a[i])
for i in range(m):
    s, t = map(int, input().split())
    s -= 1
    t -= 1   
    if s < t:
        print(right[t] - right[s])
    else:
        print(left[t] - left[s])
