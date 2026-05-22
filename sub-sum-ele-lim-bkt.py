n,t,k=map(int,input().split())
a=list(map(int,input().split()))
def f(i,s,c,p):
    if s==t and c<=k:
        print("["+" ".join(map(str,p))+"]")
        return
    if i==n or s>t or c>k: return
    f(i+1,s+a[i],c+1,p+[a[i]])
    f(i+1,s,c,p)
f(0,0,0,[])
