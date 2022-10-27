# DSLR
from collections import deque

# visited = [0] * 10000   # TC 마다 visitied 초기화 필요


def bfs(a, b):
    q = deque()
    q.append((a, ""))
    visited = [0] * 10000  # 10,000 미만의 십진수
    visited[a] = 1

    while q:
        tmp, ops = q.popleft()
        if tmp == b:
            print(ops)
            break

        opsD = (tmp * 2) % 10000
        if not visited[opsD]:
            visited[opsD] = 1
            q.append((opsD, ops + "D",))

        opsS = tmp - 1 if tmp != 0 else 9999
        if not visited[opsS]:
            visited[opsS] = 1
            q.append((opsS, ops + "S"))

        # 1 -> 10 / 123 -> 1230
        opsL = 10 * (tmp % 1000) + (tmp // 1000)
        if not visited[opsL]:
            visited[opsL] = 1
            q.append((opsL, ops + "L"))

        # 1 -> 1000 / 123 -> 3012
        opsR = 1000 * (tmp % 10) + tmp // 10
        if not visited[opsR]:
            visited[opsR] = 1
            q.append((opsR, ops + "R"))


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    bfs(a, b)
