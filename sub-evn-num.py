n,t=map(int,input().split())
a=list(map(int,input().split()))
ans=[]
def d(i,s,p):
    if s==t and len(p)%2==0:
        ans.append(tuple(p))
    if i==n or s>t: return
    d(i+1,s+a[i],p+[a[i]])
    d(i+1,s,p)
d(0,0,[])
if not ans:
    print(0)
else:
    for x in sorted(set(ans)):
        print("["+" ".join(map(str,x))+"]")