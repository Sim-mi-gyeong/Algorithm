# 퇴사
# 뒤에서 부터 접근! 
# N 번째 날 = [ (N + 1) 번째 날 기준 수익(dp) ] 과 [ N 번째 날 수익 + (Tn) 만큼 지난 후 수익] 중 큰 값

# 예를 들어 5일 째인 날에 3일이 걸리는 건 할 수 있지 않나 ? 그러니까, i + (t-1) > n 이 되어야 하지 않는가 ?
# -> 그렇지만, dp 테이블에서 i + t 를 계산할 때 -1 해주지 않으면 인덱스 오류 
# 또한, i 는 인덱스이므로 n 보다 -1 작은 값 & 여기서 t-1 까지 해주면 마지막 7번째 날에 대한 값까지 인정되어 dp 테이블에 반영 -> if i + t-1 >= n:

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)

for i in range(n-1, -1, -1):
    t, p = lst[i][0], lst[i][1]
    if i + t > n: 
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+t] + p)
print(dp[0])