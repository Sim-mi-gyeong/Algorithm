# 말이 되고픈 원숭이

from collections import deque
import sys

input = sys.stdin.readline
k = int(input())
w, h = map(int, input().split())
dx1 = [-2, -1, 1, 2, 2, 1, -1, -2]
dy1 = [1, 2, 2, 1, -1, -2, -2, -1]
dx2, dy2 = [-1, 1, 0, 0], [0, 0, -1, 1]

graph = [list(map(int, input().split())) for _ in range(h)]
visited = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]
ans = int(1e9)


def bfs(startX, startY):
    global ans
    q = deque()
    visited[startX][startY][0] = 1
    q.append((startX, startY, 0, 0))

    while q:
        x, y, cnt, tmpK = q.popleft()
        if x == h - 1 and y == w - 1:
            ans = min(ans, cnt)
            return ans

        if tmpK < k:
            for i in range(len(dx1)):
                nx = x + dx1[i]
                ny = y + dy1[i]
                if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != 1:
                    if visited[nx][ny][tmpK + 1]:
                        continue
                    else:
                        visited[nx][ny][tmpK + 1] = 1
                        q.append((nx, ny, cnt + 1, tmpK + 1))

        # 말의 이동 방법이 아닌, 원숭이 이동 방법은 횟수 상관없이 가능
        for j in range(len(dx2)):
            nx = x + dx2[j]
            ny = y + dy2[j]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != 1:
                if visited[nx][ny][tmpK]:
                    continue
                else:
                    visited[nx][ny][tmpK] = 1
                q.append((nx, ny, cnt + 1, tmpK))

    return -1


print(bfs(0, 0))
