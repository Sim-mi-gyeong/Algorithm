# 쉬운 계단 수 

# n = int(input())
# dp = [0] * 10
# if n == 1:
#     for i in range(1, 10):
#         dp[i] = 1
# else:
#     for _ in range(n-1):
#         for i in range(1, 9):
#             dp[i] += 1
#         for j in range(9, 1-1, -1):
#             dp[j] += 1
# print(sum(dp) % 1000000000)

n = int(input())
dp = [[0] * 10 for _ in range(n+1)]
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2, n+1):
    for j in range(0, 10):   # 끝자리
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else: dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[n]) % 1000000000)