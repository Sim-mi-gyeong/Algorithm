# 오르막 수

n = int(input())
dp = [0] * (10 + 1)
for i in range(1, 10+1):
    dp[i] = 1
if n == 1:
    print(sum(dp))
else:
    for _ in range(n):
        for i in range(2, 10+1):
            dp[i] = dp[i-1] + dp[i]   # dp[i] = 이전 회차의 dp 에서 i번째까지 원소의 합과 같음
    print(dp[10] % 10007)