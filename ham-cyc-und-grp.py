n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
path = [0]
vis = [0] * n
vis[0] = 1
def dfs(v):
    if len(path) == n:
        if g[v][0]:
            print(*path, 0, end="")
            return 1
        return 0
    for i in range(1, n):
        if g[v][i] and not vis[i]:
            vis[i] = 1
            path.append(i)
            if dfs(i):
                return 1
            vis[i] = 0
            path.pop()
    return 0
if not dfs(0):
    print("Solution does not exist", end="")