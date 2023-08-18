# 구간 나누기 2

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))


def divide(x):
    maxVal = minVal = arr[0]
    cnt = 1
    for i in range(1, n):
        maxVal = max(maxVal, arr[i])
        minVal = min(minVal, arr[i])
        if maxVal - minVal > x:
            cnt += 1
            maxVal = arr[i]
            minVal = arr[i]

    return cnt


start, end = 0, max(arr)
ans = 0
while start <= end:
    mid = (start + end) // 2
    if divide(mid) <= m:
        end = mid - 1
        ans = mid
    else:
        start = mid + 1

print(ans)