n=int(input())

l = [ int(input()) for i in range(n)]
t = int(input())
dp = [[0 for i in range(t+1)] for j in range(n+1)]
dp[0][0]=1
for i in range(1,t+1):
    dp[0][i]=0

for i in range(1,n+1):
    dp[i][0]=1

for i in range(1,n+1):
    for j in range(1,t+1):
        
        if dp[i-1][j]==1 or (j-l[i-1]>-1 and dp[i-1][j - l[i-1]]==1):
            
            dp[i][j]=1
        else:
            dp[i][j]=0


if dp[n][t]==1:
    print("true")
else:
    print("false")