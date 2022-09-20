# 공주님을 구해라! -> 그람 찾기를 먼저 시도
from collections import deque
import sys

input = sys.stdin.readline
n, m, t = map(int, input().split())

graph = []
for i in range(n):
    tmp = list(input().split())
    graph.append(tmp)
    for j in range(len(tmp)):
        if tmp[j] == "2":
            gramX, gramY = i, j

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
have = False


def findGram(startX, startY):
    global have
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append((startX, startY, 0))
    visited[startX][startY] = 1

    while q:
        x, y, cnt = q.popleft()
        if x == gramX and y == gramY:
            have = True
            return cnt
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    if graph[nx][ny] != "1":
                        q.append((nx, ny, cnt + 1))
                        visited[nx][ny] = 1
    return 0


gramCnt = findGram(0, 0)


def bfs(visited, have, use, startX, startY):

    q = deque()
    q.append((startX, startY))
    while q:
        x, y = q.popleft()
        if x == n - 1 and y == m - 1:
            if visited[x][y] <= t:
                return visited[x][y]
            else:
                "Fail"
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    if graph[nx][ny] != "1":
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
                    elif graph[nx][ny] == "1":
                        if have:
                            if use:
                                visited[nx][ny] = visited[x][y] + 1
                                q.append((nx, ny))

    return "Fail"


visited = [[0] * m for _ in range(n)]
if gramCnt != 0:
    originTime = bfs(visited, have, False, 0, 0)
    visited = [[0] * m for _ in range(n)]
    visited[gramX][gramY] = gramCnt
    gramTime = bfs(visited, have, True, gramX, gramY)
    if originTime == "Fail":
        print(gramTime)
    else:
        print(min(originTime, gramTime))
else:
    originTime = bfs(visited, have, False, 0, 0)
    print(originTime)


"""
5 4 100
0 1 2 1
0 1 0 1
0 0 0 0
1 1 1 1
0 0 0 0

answer : 11

5 3 100
0 1 2 
0 1 1 
0 0 0 
0 1 0 
0 0 0 

answer : 6

4 10 100
0 1 1 1 1 2 1 1 1 1
0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 0

answer : 14

4 4 10
0 0 0 0
0 0 1 0
0 1 2 1
0 0 0 0

answer : 6

3 3 100
0 1 2
0 1 1
0 0 0

answer : 4

[오답 확인한 반례] -> t 에 대한 조건 체크를 안한 것,,
3 3 1
0 1 0
2 1 0
0 1 0

answer : Fail

"""

