def unbounded_knapSack(W, wt, val, n):
    
    dp = [0 for i in range(W+1)]
    
    for i in range(n):
        
        for j in range(W+1):
            
            if wt[i]<=j:
                
                dp[j]=max(dp[j-wt[i]]+val[i],dp[j])
    return dp[W]            
            
    

# write your code here

n = int(input())

val = list(map(int,input().split()))
wt = list(map(int,input().split()))
W = int(input()) 
 
 