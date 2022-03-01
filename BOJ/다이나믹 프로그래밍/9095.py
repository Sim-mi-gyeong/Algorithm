# 1, 2, 3 더하기

t = int(input())
dp = [0] * 11
dp[1], dp[2], dp[3] = 1, 2, 4

for _ in range(t): 
    n = int(input())
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] +  dp[i-3]
    print(dp[n])