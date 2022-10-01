# 벽 부수고 이동하기 2

from collections import deque
import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(startX, startY):
    q = deque()
    visited[startX][startY][0] = 1
    q.append((startX, startY, 1, 0))

    while q:
        x, y, cnt, tmpK = q.popleft()
        if x == n - 1 and y == m - 1:
            return cnt

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if tmpK < k:
                    if graph[nx][ny] == 1 and visited[nx][ny][tmpK + 1] == 0:
                        visited[nx][ny][tmpK + 1] = 1
                        q.append((nx, ny, cnt + 1, tmpK + 1))

                if graph[nx][ny] == 0 and visited[nx][ny][tmpK] == 0:
                    visited[nx][ny][tmpK] = 1
                    q.append((nx, ny, cnt + 1, tmpK))
    return -1


print(bfs(0, 0))


"""

4 4 2
0111
1101
0001
0110
answer : 7

4 2 1
01
00
11
10
answer : 5

"""
