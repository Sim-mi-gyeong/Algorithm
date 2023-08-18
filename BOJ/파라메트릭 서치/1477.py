# 휴게소 세우기

import sys

input = sys.stdin.readline
n, m, l = map(int, input().split())

arr = [0] + list(map(int, input().split())) + [l]
arr.sort()


def check(mid):
    cnt = 0
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] > mid:
            cnt += (arr[i + 1] - arr[i] - 1) // mid
    return cnt


start, end = 1, l
while start <= end:
    mid = (start + end) // 2

    if check(mid) <= m:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)
