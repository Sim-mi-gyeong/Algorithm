# 퇴사
# https://mygumi.tistory.com/151

# dp[N] = N 일까지 얻는 이익
# N 일 기준으로 N 일 이전에 얻을 수 있는 경우 모두 비교
# dp[i] = max(p[i] + dp[j], dp[i]) (i : 기준일, j : (1 ~ (i-1) 일))

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)
    
for i in range(2, n + 1):   # 기준일에 대해
    for j in range(1, i):   # 기준일까지에 대해 
        t = lst[j-1][0]  
        p = lst[i-1][1] 
        if (i - j >= t): dp[i] = max(dp[i], dp[j] + p)

        
print(max(dp))