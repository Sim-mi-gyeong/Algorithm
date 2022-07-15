# 소문난 칠공주

from collections import deque
from itertools import combinations

n = 5
graph = [list(input()) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(comb):
    q = deque()
    startX, startY = comb[0][0], comb[0][1]
    q.append((startX, startY))

    visited = [0] * 7
    startIndex = comb.index((startX, startY))
    visited[startIndex] = 1

    while q:
        x, y = q.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위는 넘어가지 않는 것이 보장됨 !
            # 다음으로 이동한 위치가 리스트 조합에 존재하는 위치여야 함 !
            if (nx, ny) in comb:
                nextIndex = comb.index((nx, ny))
                if not visited[nextIndex]:
                    visited[nextIndex] = 1
                    q.append((nx, ny))

    if False in visited:
        return False

    return True


def checkCnt(lst):
    tmp = 0
    for i in range(len(lst)):
        row = lst[i][0]
        col = lst[i][1]

        if graph[row][col] == "S":
            tmp += 1

    if tmp >= 4:
        return True

    return False


ans = 0
tmpList = [(i, j) for i in range(n) for j in range(n)]
combList = list(combinations(tmpList, 7))

for comb in combList:
    if checkCnt(comb):
        if bfs(comb):
            ans += 1

print(ans)
