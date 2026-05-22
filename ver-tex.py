def is_cover(edges, cover):
    for u, v in edges:
        if u not in cover and v not in cover:
            return False
    return True
n, m = map(int, input().split())
edges = []
vertices = set()
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))
    vertices.add(u)
    vertices.add(v)
vertices = list(vertices)
best = vertices
for mask in range(1 << len(vertices)):
    cover = set()
    for i in range(len(vertices)):
        if mask & (1 << i):
            cover.add(vertices[i])
    if is_cover(edges, cover):
        if len(cover) < len(best):
            best = list(cover)
print(*sorted(best), end="")