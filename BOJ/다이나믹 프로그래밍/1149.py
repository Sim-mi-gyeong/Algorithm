# RGB 거리

n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):   # 1번 집부터 ~ 행을 따라
    for j in range(3):   # R G B
        # 현재 위치가 R 열이라면, 
        if j == 0:
            before = min(dp[i-1][1], dp[i-1][2])
        # 현재 위치가 G 열이라면, 
        elif j == 1:
            before = min(dp[i-1][0], dp[i-1][2])
        # 현재 위치가 B 열이라면,
        elif j == 2:
            before = min(dp[i-1][0], dp[i-1][1])
        dp[i][j] = dp[i][j] + before

# for i in range(1, n):   # 1번 집부터 ~ 행을 따라
#     dp[i][0] = dp[i][0] + min(dp[i-1][1], dp[i-1][2])
#     dp[i][1] = dp[i][1] + min(dp[i-1][0], dp[i-1][2])
#     dp[i][2] = dp[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))