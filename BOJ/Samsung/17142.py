# 연구소 3

from collections import deque
import copy
from itertools import combinations

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
virusList = []
virusCnt = 0
wallCnt = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virusList.append((i, j))
            virusCnt += 1
        elif graph[i][j] == 1:
            wallCnt += 1

empty = n * n - (virusCnt + wallCnt)
if empty == 0:
    print(empty)
    exit(0)

combinationVirusList = list(combinations(virusList, m))


def bfs(combinationVirus, newGraph, visited):
    global emptyTrans
    q = deque()

    for virus in combinationVirus:
        visited[virus[0]][virus[1]] = 1
        q.append((virus[0], virus[1], 0))

    ans = 0

    while q:
        x, y, time = q.popleft()
        if newGraph[x][y] == 2:
            newGraph[x][y] = time
            visited[x][y] = 1

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] != 1:
                if newGraph[nx][ny] == 0:
                    emptyTrans += 1
                    newGraph[nx][ny] = newGraph[x][y] + 1
                    visited[nx][ny] = 1
                    q.append((nx, ny, time + 1))
                    ans = max(ans, time + 1)
                elif newGraph[nx][ny] == 2:
                    newGraph[nx][ny] = newGraph[x][y] + 1
                    visited[nx][ny] = 1
                    q.append((nx, ny, time + 1))
                    ans = max(ans, time + 1)

        if (
            emptyTrans >= empty
        ):  # 모든 칸에 바이러스가 퍼지는 최소 시간을 구할 때, 활성 상태 바이러스가 비활성 상태인 바이러스 자리까지 도달하는 데에 걸리는 시간은 고려하지 않는다.
            break

    if emptyTrans < empty:
        ans = 1e9

    return ans


minVal = 1e9
for combinationVirus in combinationVirusList:
    visited = [[0] * n for _ in range(n)]
    newGraph = copy.deepcopy(graph)
    emptyTrans = 0

    tmpVal = bfs(combinationVirus, newGraph, visited)
    minVal = min(minVal, tmpVal)

if minVal == 1e9:
    print(-1)
else:
    print(minVal)


"""
9 1
0 2 2 2 2 2 2 2 0
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1

정답 : 4

5 1
0 2 2 2 2
0 1 2 2 2
0 1 2 2 2
0 1 2 2 2
0 1 2 2 1

정답 : 5

4 4
1 1 1 1
1 2 2 1
1 2 2 1
1 1 1 1

정답 : 0

5 1 
1 1 1 1 1 
1 1 1 1 1 
1 1 1 1 1 
0 2 0 2 0 
1 1 1 1 1

정답 : 3
"""
