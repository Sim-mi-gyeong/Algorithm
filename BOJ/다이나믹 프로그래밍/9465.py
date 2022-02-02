# 스티커

t = int(input())
for i in range(t):
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(2)]
    dp = s
    for j in range(1, n):   # 1열부터 ~ n-1(열 최대)열 까지
        
        left_down = dp[1][j-1]   # 현재 행이 0행이면, 이전은 1행 left_down
        left_up = dp[0][j-1]    # 현재 행이 1행이면, 이전은 0향 left_up
        # 해당 열에서 선택을 하지 않으면, 다음 열에서는 left_down / left_up 무관
        if j < 2:
            dp[0][j] = dp[0][j] + left_down
            dp[1][j] = dp[1][j] + left_up
        else:
            dp[0][j] = max(dp[0][j] + left_down, max(dp[0][j-2], dp[1][j-2]) + dp[0][j])   # 현재 열은 업데이트 하지 않고, 다음 열을 위해 넘어갈 수 있음
            dp[1][j] = max(dp[1][j] + left_up, max(dp[0][j-2], dp[1][j-2]) + dp[1][j])

    ans = 0
    for i in range(2):
        ans = max(ans, dp[i][n-1])
    print(ans)