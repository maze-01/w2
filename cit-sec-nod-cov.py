from itertools import combinations
n, m, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
def is_cover(cover):
    for u, v in edges:
        if u not in cover and v not in cover:
            return False
    return True
found = False
for r in range(k + 1):
    for comb in combinations(range(n), r):
        cover = set(comb)
        if is_cover(cover):
            print("Yes")
            for x in sorted(cover):
                print(x, end=" ")
            found = True
            break
    if found:
        break
if not found:
    print("No")