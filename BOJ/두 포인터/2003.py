# 수들의 합2

n, m = map(int, input().split())
lst = list(map(int, input().split()))
end = 0
cnt = 0
sumValue = 0   # m 과 비교할 값

for start in range(n):
    while sumValue < m and end < n:
        sumValue += lst[end]
        end += 1
    if sumValue == m:
        cnt += 1
    sumValue -= lst[start]
print(cnt)