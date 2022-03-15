# 가장 큰 증가 부분 수열

n = int(input())
lst = list(map(int, input().split()))

dp = [0] * n
for i in range(len(lst)): dp[i] = lst[i]
for i in range(1, n):
    for j in range(0, i):
        if lst[j] < lst[i]:
            # 이렇게 하면, 이미 이전 j 에서 처리가 된 dp[i]에 + lst[j]가 되므로, 비교 대상의 값이 계속해서 바뀌게 됨
            # -> 즉, 특정 i 일때 dp[i]값이 계속해서 증가하 것
            # dp[i] = max(dp[i], dp[i] + lst[j])  
            dp[i] = max(dp[i], dp[j] + lst[i])
print(max(dp))