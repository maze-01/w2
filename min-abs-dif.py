from itertools import combinations
n=int(input())
a=list(map(int,input().split()))
sz1=(n+1)//2 if n%2 else n//2
best=(10**9,10**9,[]) 
for idxs in combinations(range(n),sz1):
    s1=sum(a[i] for i in idxs)
    s2=sum(a)-s1
    diff=abs(s1-s2)
    cand=(diff, min(s1,s2), idxs if s1<=s2 else tuple(i for i in range(n) if i not in idxs))
    if cand<best: best=cand
chosen=set(best[2])
sub1=[a[i] for i in range(n) if i in chosen]
sub2=[a[i] for i in range(n) if i not in chosen]
print(*sub1,end=" ");print()
print(*sub2,end=" ");print()