# 퇴사
# 지금 당장에는 더 좋을지라도, 이후와 비교했을 때에는 불리한 경우 -> 평범한 배낭 문제와 유사 ? 
# 순서와 시간 + 이익 요소 고려

# 현재 시점인 i 에서 상담을 시작했을 때 걸리는 각 상담일 t[i] 를 더해 -> 범위를 초과하지 않는 경우, dp 테이블에 해당 금액 p[i] 를 더해줌

# 상담을 통한 이익은, 상담을 종료한 시점에 얻게 된다는 것을 적용
# -> 이후, 상담이 지속되는 동안 이익 금액도 유지되도록 테이블에 값을 추가

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)
for i in range(n):
    t = lst[i-1][0]   # 기간
    p = lst[i-1][1]   # 이익
    if i + t > n : continue
    else:
        dp[i + t] = max(dp[i + t], dp[i] + p)
    # 상담은 중간에 그만두는 것이 아니라 지속되기 때문에 ->  금액도 유지되도록
    dp[i+1] = max(dp[i], dp[i+1])
print(max(dp))

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+2)
for i in range(1, n+1):
    t = lst[i-1][0]   # 기간
    p = lst[i-1][1]   # 이익
    if i + t > n+1 : continue
    else:
        dp[i + t] = max(dp[i + t], dp[i] + p)
    # 각 인덱스 테이블 값을 최댓값으로 유지하되, 종료일 이후의 이익은 누적되도록 
    dp[i+1] = max(dp[i], dp[i+1])
print(max(dp))