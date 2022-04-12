# 부분 삼각 수열

from itertools import combinations
import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0

if len(a) < 3:
    print(len(a))
    exit(0)

for i in range(3, n + 1):
    lst = list(combinations(a, i))

    if len(lst[0]) == 3:
        checkCnt = 0
        for j in range(len(lst)):
            x, y, z = lst[j][0], lst[j][1], lst[j][2]
            if x + y > z and x + z > y and y + z > x:
                checkCnt += 1
            if checkCnt > 0:
                length = i
                break

    else:
        # 여기서 또 3개씩 조합 생성
        for j in range(len(lst)):
            checkCnt = 0
            sub = list(combinations(lst[j], 3))
            for k in range(len(sub)):
                x, y, z = sub[k][0], sub[k][1], sub[k][2]
                if x + y > z and x + z > y and y + z > x:
                    checkCnt += 1
            if checkCnt == len(sub):
                length = i

    if ans <= length:
        ans = length

print(ans)
