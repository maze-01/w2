a = list(map(int, input().split()))
t = int(input())
a.sort()
ans = []
def dfs(i, s, path):
    if s == t:
        ans.append(path[:])
        return
    if s > t or i == len(a):
        return
    path.append(a[i])
    dfs(i, s + a[i], path)
    path.pop()
    dfs(i + 1, s, path)
dfs(0, 0, [])
print(ans, end="")