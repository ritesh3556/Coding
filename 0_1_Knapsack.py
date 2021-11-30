def zeroknapSack(W, wt, val, n):
    
    dp = [[0 for i in range(W+1)] for j in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,W+1):
            
            if wt[i-1]<=W:
                if j-wt[i-1]>=0:
                    
                    dp[i][j] = max(dp[i-1][j],dp[i-1][j-wt[i-1]]+val[i-1])
                else:
                    dp[i][j]=dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    
    
    return dp[n][W]            
                

# write your code here


n = int(input())

val = list(map(int,input().split()))
wt = list(map(int,input().split()))
W=int(input())


print(zeroknapSack(W, wt, val, n))