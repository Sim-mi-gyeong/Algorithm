# 미네랄

from collections import deque
import sys

input = sys.stdin.readline

r, c = map(int, input().split())
graph = []
for _ in range(r):
    tmp = list(input().rstrip())
    graph.append(tmp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()


def throw(h, turn):
    height = r - h
    targetX, targetY = height, 0

    if turn % 2 == 0:
        for j in range(c):
            if graph[height][j] == "x":
                graph[height][j] = "."
                targetY = j
                break

    else:
        for j in range(c - 1, -1, -1):
            if graph[height][j] == "x":
                graph[height][j] = "."
                targetY = j
                break

    for i in range(len(dx)):
        nx = targetX + dx[i]
        ny = targetY + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if graph[nx][ny] == "x":
                q.append((nx, ny))


def find_cluster_and_gravity(x, y):
    queue = deque()
    visited = [[0] * c for _ in range(r)]

    visited[x][y] = 1
    queue.append((x, y))
    cluster_list = []

    while queue:
        x, y = queue.popleft()
        if x == r - 1:
            return
        if graph[x + 1][y] == ".":
            cluster_list.append((x, y))

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and graph[nx][ny] == "x":
                visited[nx][ny] = 1
                queue.append((nx, ny))

    gravity(visited, cluster_list)


def gravity(visited, cluster_list):

    gravity_cnt, check = 1, False
    while True:
        for i, j in cluster_list:
            if i + gravity_cnt == r - 1:
                check = True
                break
            if graph[i + gravity_cnt + 1][j] == "x" and not visited[i + gravity_cnt + 1][j]:
                check = True
                break
        if check:
            break
        gravity_cnt += 1

    for i in range(r - 2, -1, -1):
        for j in range(c):
            if graph[i][j] == "x" and visited[i][j]:
                graph[i + gravity_cnt][j] = "x"
                graph[i][j] = "."


n = int(input())
lst = list(map(int, input().split()))
turn = 0
for i in range(n):
    h = lst[i]
    throw(h, turn)

    while q:
        x, y = q.popleft()
        find_cluster_and_gravity(x, y)

    turn += 1

for i in range(r):
    print(*graph[i], sep="")
