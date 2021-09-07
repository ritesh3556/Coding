



n = int(input())
l = [int(input()) for i in range(n)]

t = int(input())

dp = [0 for i in range(t+1)]

dp[0]=1

for i in range(n):
    
    j = l[i]
    while(j<t+1):
        
        if j-l[i]>-1:
            dp[j]+=dp[j-l[i]]
        j+=1

print(dp[t])        
