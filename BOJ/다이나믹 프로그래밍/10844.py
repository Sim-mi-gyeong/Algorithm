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

a, b = map(int, input().split())
print(a*b)