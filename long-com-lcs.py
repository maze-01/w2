x=input()
y=input()
z=input()
a,b,c=len(x),len(y),len(z)
dp=[[[0]*(c+1) for _ in range(b+1)] for _ in range(a+1)]
for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            if x[i-1]==y[j-1]==z[k-1]:
                dp[i][j][k]=dp[i-1][j-1][k-1]+1
            else:
                dp[i][j][k]=max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])
print(dp[a][b][c],end="")