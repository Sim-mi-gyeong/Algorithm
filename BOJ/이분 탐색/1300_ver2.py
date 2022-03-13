# K번째 수

n = int(input())
k = int(input())

start, end = 1 * 1, n * n
while start <= end:
    mid = (start + end) // 2
    ans = 0
    for i in range(1, n+1):
        ans += min(mid // i, n)
    if ans >= k:
        end = mid - 1
        result = mid
    else:
        start = mid + 1
print(result)