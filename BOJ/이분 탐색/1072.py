# 게임
# x 를 증가 -> y도 증가 -> 승률 증가

import math

x, y = map(int, input().split())
z = math.floor((y / x) * 100)
if z >= 100:
    print(-1)
    exit(0)

start = x
end = 1000000000
print("처음 승률 z : ", z)


def binarySearch(x, y, start, end):
    ans = 1000000000
    # result = 0
    while start <= end:
        mid = (start + end) // 2
        # 최소 몇 판 더 해야하는지
        newY = y + (mid - start)
        nextZ = math.floor((newY / mid) * 100)
        if nextZ <= z:
            start = mid + 1
        else:
            end = mid - 1
            result = end
            print("result : ", result, "승률 : ", nextZ)

        ans = min(ans, result)

    return ans


ans = binarySearch(x, y, start, end) - x
print(ans)
