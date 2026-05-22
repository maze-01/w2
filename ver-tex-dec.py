from itertools import combinations
n, m, k = map(int, input().split())
e = [tuple(map(int, input().split())) for _ in range(m)]
f = 0
for r in range(k + 1):
    for c in combinations(range(n), r):
        s = set(c)
        if all(u in s or v in s for u, v in e):
            f = 1
            break
    if f:
        break
print("YES" if f else "NO", end="")