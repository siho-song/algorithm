import sys
input = sys.stdin.readline

max = 100
mod = 1000000000
dp =[[0]*10 for _ in range(max+1)]
dp[1] = [1]*10

n=int(input())

for n in range(2,n+1):
    for i in range (0,10):
        if i==0:
            dp[n][i] = dp[n-1][1]%mod  
        elif i==9:
            dp[n][i] = dp[n-1][8]%mod  
            
        else :
            dp[n][i] = dp[n-1][i-1]%mod + dp[n-1][i+1]%mod
print((sum(dp[n])-dp[n][0])%mod)

