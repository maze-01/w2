n=int(input())
b=[[0]*n for _ in range(n)]
c=[0]*n
d1=[0]*(2*n); d2=[0]*(2*n)
def f(r):
    if r==n:return 1
    for i in range(n):
        x=r-i+n
        y=r+i
        if c[i]|d1[x]|d2[y]:continue
        b[r][i]=c[i]=d1[x]=d2[y]=1
        if f(r+1):return 1
        b[r][i]=c[i]=d1[x]=d2[y]=0
    return 0
f(0)
for i in b:
    print(i)