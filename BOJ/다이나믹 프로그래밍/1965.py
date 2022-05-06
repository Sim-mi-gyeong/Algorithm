# 상자넣기

n = int(input())
dp = [1] * n
lst = list(map(int, input().split()))

for i in range(1, len(lst)):
    for j in range(0, i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

