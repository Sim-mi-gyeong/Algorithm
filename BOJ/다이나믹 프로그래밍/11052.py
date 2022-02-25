# 카드 구매하기

n = int(input())
lst = [0]
lst = lst + list(map(int, input().split()))
dp = [0] * (n+1)
if n == 1:
    dp[1] = lst[1]
else:
    dp[1] = lst[1]
    dp[2] = max(dp[1] + dp[1], lst[2])
    for i in range(3, n+1):
        # 각 부분에서 경우의 수가 세 가지 -> 구조 나타내기
        for j in range(1, i+1):
            dp[i] = max(dp[i], dp[i-j] + lst[j])
            
        # if i % 2 == 0:   # 짝수
        #     dp[i] = max(lst[i], dp[i-1] + lst[1], dp[i//2] * 2)
        # else: dp[i] = max(lst[i], dp[i-1] + lst[1])   # 홀수

print(dp[n])