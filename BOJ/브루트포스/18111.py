# 마인크래프트

import sys

input = sys.stdin.readline
n, m, b = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
INF = 1e9
ansTime = INF
minH = min(min(lst))
maxH = max(max(lst))
for h in range(minH, maxH + 1):
    cnt1, cnt2 = 0, 0
    for i in range(n):
        for j in range(m):
            d = lst[i][j] - h
            if d > 0:
                cnt1 += abs(d)
            elif d < 0:
                cnt2 += abs(d)
                # if b >= d:
                #     cnt2 += abs(d)
                # else:
                #     continue

    if b + cnt1 >= cnt2:
        time = cnt1 * 2 + cnt2
        if ansTime >= time:
            ansTime = time
            ansHeight = h

print(ansTime, ansHeight)

# 바로 시간을 비교하지 말고, 1번과 2번을 각각 수행한 count 세기
# 인벤토리 블록의 개수에 따라 2번 연산 수행 가능 여부 결정 -> 리스트 각 원소마다 필요한 개수 구해보고 -> 가능하다면 연산 수행 처리
