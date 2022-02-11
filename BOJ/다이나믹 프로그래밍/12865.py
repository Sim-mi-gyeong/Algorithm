# 평범한 배낭
# 냅색(Knapsack) 알고리즘
# 물건을 배낭에 담을 때, 
# 1. 현재 배낭의 허용 무게 < 넣을 물건의 무게가 더 크면 넣지 않는다.
# 2. 그렇지 않을 경우, 즉 배낭의 무게가 여유있는 경우
# 2-1. 현재 넣을 물건의 무게만큼 배낭에서 빼고 -> 현재 물건을 넣는다.
# 2-2. 현재 물건을 넣지 않고 이전 배낭을 그대로 가지고 간다.

# d[n][k]는 N번째 물건 까지 살펴보았을 때, 무게가 K인 배낭의 최대 가치

# 순차적으로 더해지는 게 아니라, 여러 가지 중 조합을 해서 최댓값을 만드는 것

n, k = map(int, input().split())
lst = [[0, 0]]
for i in range(n):
    lst.append(list(map(int, input().split())))
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):   # i : 현재 담을 물건의 idx
    for j in range(1, k+1):   # j : 현재 가방의 허용 무게 
        w = lst[i][0]
        v = lst[i][1]
        if j < w:   # 현재 넣을 물건의 무게가 더 크면 -> 넣지 X
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
print(dp[n][k])