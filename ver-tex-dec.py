def vertex_cover(edges, k):
    if not edges:
        return True
    if k == 0:
        return False
    u, v = next(iter(edges))
    e1 = {e for e in edges if u not in e}
    e2 = {e for e in edges if v not in e}
    return vertex_cover(e1, k - 1) or vertex_cover(e2, k - 1)
n, m, k = map(int, input().split())
edges = set()
for _ in range(m):
    u, v = map(int, input().split())
    edges.add((u, v))
print("YES" if vertex_cover(edges, k) else "NO")