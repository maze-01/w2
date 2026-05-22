from itertools import permutations
n=int(input())
g=[list(map(int,input().split())) for _ in range(n)]
a=10**9
p=[]
for x in permutations(range(1,n)):
    t=[0]+list(x)+[0]
    c=0
    for i in range(n):
        if g[t[i]][t[i+1]]==0:
            c=10**9
            break
        c+=g[t[i]][t[i+1]]
    if c<a:
        a=c
        p=t
print(a)
print(*p,end="")