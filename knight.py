from collections import deque
sx, sy = map(int, input().split())
tx, ty = map(int, input().split())
d = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
q = deque([(sx, sy, 0)])
v = {(sx, sy)}
while q:
    x, y, s = q.popleft()
    if (x, y) == (tx, ty):
        print(s, end="")
        break
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 1 <= nx <= 8 and 1 <= ny <= 8 and (nx, ny) not in v:
            v.add((nx, ny))
            q.append((nx, ny, s + 1))