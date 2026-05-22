n=int(input())
a=[0]*n
f=0
def ok(r,c):
    for i in range(c):
        if a[i]==r or abs(a[i]-r)==abs(i-c):
            return 0
    return 1
def solve(c):
    global f
    if c==n:
        print(*a)
        f=1
        return
    for r in range(n):
        if ok(r,c):
            a[c]=r
            solve(c+1)
solve(0)
if not f:
    print(-1)