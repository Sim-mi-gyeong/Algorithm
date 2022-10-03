from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
limit = 1


def bfs(startX, startY):
    q = deque()
    visited[startX][startY][0] = 1
    q.append((startX, startY, 1, 0))

    while q:
        x, y, cnt, tmpLimit = q.popleft()
        if x == n - 1 and y == m - 1:
            return cnt

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if tmpLimit < limit:
                    if graph[nx][ny] == 1 and not visited[nx][ny][tmpLimit + 1]:
                        visited[nx][ny][tmpLimit + 1] = 1
                        q.append((nx, ny, cnt + 1, tmpLimit + 1))

                if graph[nx][ny] == 0 and not visited[nx][ny][tmpLimit]:
                    visited[nx][ny][tmpLimit] = 1
                    q.append((nx, ny, cnt + 1, tmpLimit))

    return -1


print(bfs(0, 0))


"""
5 5
00100
11000
00110
01011
00000

answer : 9
"""

