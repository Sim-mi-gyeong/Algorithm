# 이친수

# n = int(input())
# dp = [''] * n
# dp[0] += '1'
# dp[1] += '0'

# for i in range(2, n):
#     for j in range(len(dp[i-1])):
#         if dp[i-1][j] == '1':
#             dp[i] += '0'
#         else:
#             dp[i] += '0'
#             dp[i] += '1'
# print(len(dp[n-1]))

n = int(input())
dp = [0] * (n+1)
if n == 1: dp[1] = 1   # n = 1 일 때 체크를 하지 않으면 dp[2]를 할당하지 못해 런타임 에러 발생
else:
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
print(dp[n])