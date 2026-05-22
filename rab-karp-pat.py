T=input().strip()
P=input().strip()
n,m=len(T),len(P)
if m>n: print("No Match"); exit()
B=256; M=10**9+7
hp=ht=0; powB=pow(B,m-1,M)
for i in range(m):
    hp=(hp*B+ord(P[i]))%M
    ht=(ht*B+ord(T[i]))%M
ans=[]
for i in range(n-m+1):
    if hp==ht and T[i:i+m]==P: ans.append(str(i))
    if i<n-m:
        ht=((ht-ord(T[i])*powB)%M*B + ord(T[i+m]))%M
print(' '.join(ans) if ans else "No Match")