




n = int(input())
l=[int(input()) for i in range(n)]

dp = [None]*(n+1)
dp[n]=0
i=n-1
while(i>-1):
    
    j=1
    mi = 1231313
    while(j<=l[i]):
        
        if i+j<=n and dp[i+j]!=None:
            mi=min(mi,dp[i+j])
            
        
        j+=1
    if mi != 1231313:
        dp[i]=mi+1
    
    
    i-=1
print(dp[0])    