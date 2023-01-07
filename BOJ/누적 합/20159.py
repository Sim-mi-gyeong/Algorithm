# 동작 그만. 밑장 빼기냐?

n = int(input())
lst = list(map(int, input().split()))
junghoonNormalSum = sum(lst[i] for i in range(0, n, 2))

maxVal = 0
junghoonExtraSum = junghoonNormalSum
for i in range(n - 1, 0, -2):
    junghoonExtraSum += lst[i]
    junghoonExtraSum -= lst[i - 1]
    maxVal = max(maxVal, junghoonExtraSum)


print(maxVal)
