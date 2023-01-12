from collections import deque
import sys

input = sys.stdin.readline

r, c = map(int, input().split())
graph = []
visited = [[0] * c for _ in range(r)]
q = deque()
fire = deque()

for i in range(r):
    tmp = list(input().rstrip())
    graph.append(tmp)
    for j in range(c):
        if tmp[j] == "J":
            startX, startY = i, j
            graph[startX][startY] = "."
            q.append((startX, startY))
            visited[startX][startY] = 1
        if tmp[j] == "F":
            fire.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def enableCheck(x, y):
    check = False
    if x == 0 or x == r - 1 or y == 0 or y == c - 1:
        check = True
    return check


time = 0


def bfs():
    global fire, q, time

    while True:
        time += 1
        tmpFire = deque()
        while fire:
            fireX, fireY = fire.popleft()
            for j in range(len(dx)):
                fireNx = fireX + dx[j]
                fireNy = fireY + dy[j]
                if 0 <= fireNx < r and 0 <= fireNy < c and graph[fireNx][fireNy] == ".":
                    graph[fireNx][fireNy] = "F"
                    tmpFire.append((fireNx, fireNy))
        fire = tmpFire

        tmpQ = deque()
        while q:
            x, y = q.popleft()
            if enableCheck(x, y):
                return time
            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and graph[nx][ny] == ".":
                    visited[nx][ny] = 1
                    tmpQ.append((nx, ny))
        q = tmpQ

        if not q:
            return "IMPOSSIBLE"


print(bfs())
