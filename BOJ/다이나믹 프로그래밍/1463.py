# 1로 만들기

n = int(input())
# dp[1] 일 때는 1을 만드는 연산 횟수가 0이므로 -> 0으로 초기화
dp = [0] * (n+1)
# dp[i] 는 i 번 연산했을 때의 값이 아니라 -> i인 값을 1로 만들기 위한 연산 횟수
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1   # 이 값을 채우므로 다른 값들을 1로 만드는 연산 횟수 check 가능
    if i % 2 == 0 :
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])