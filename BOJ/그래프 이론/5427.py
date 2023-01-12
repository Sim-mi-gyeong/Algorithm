# 불

from collections import deque
import sys

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(w, h, startX, startY, graph, fire):
    q = deque()
    visited = [[0] * w for _ in range(h)]

    visited[startX][startY] = 1
    q.append((startX, startY))

    time = 0
    while True:
        time += 1

        tmpFire = deque()
        while fire:
            fireX, fireY = fire.popleft()
            for i in range(len(dx)):
                fireNx = fireX + dx[i]
                fireNy = fireY + dy[i]
                if 0 <= fireNx < h and 0 <= fireNy < w and graph[fireNx][fireNy] == ".":
                    graph[fireNx][fireNy] = "*"
                    tmpFire.append((fireNx, fireNy))

        fire = tmpFire

        tmpQ = deque()
        while q:
            x, y = q.popleft()
            if x == 0 or y == 0 or x == h - 1 or y == w - 1:
                return time
            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and graph[nx][ny] == ".":
                    visited[nx][ny] = 1
                    tmpQ.append((nx, ny))

        q = tmpQ

        if not q:
            return "IMPOSSIBLE"


def solve(w, h):
    graph = []
    fire = deque()
    for i in range(h):
        tmp = list(input().rstrip())
        graph.append(tmp)
        for j in range(w):
            if tmp[j] == "@":
                startX, startY = i, j
                graph[startX][startY] = "."
            if tmp[j] == "*":
                fire.append((i, j))

    ans = bfs(w, h, startX, startY, graph, fire)
    return ans


t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    ans = solve(w, h)
    print(ans)
