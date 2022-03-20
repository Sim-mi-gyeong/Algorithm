# LCS

import sys
sys.setrecursionlimit(3000)

s1 = ' ' + input()
s2 = ' '  + input()
n1, n2 = len(s1), len(s2)
dp = [[0] * n2 for _ in range(n1)]

for i in range(1, n1):
    for j in range(1, n2):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(max(dp[n1-1]))


'''
qsdferrfgtfsawfsefeesgdtdrgthyytfgfddsdawdwd
efvs
'''

# 최장 공통 문자열(Longest Common Substring)
# for i in range(len(s1)):
#     for j in range(len(s2)):
#         if i == 0 or j == 0:
#             dp[i][j] = 0
#         elif s1[i] == s2[i]:
#             dp[i][j] = dp[i-1][j-1] + 1
#         else:
#             dp[i][j] = 0