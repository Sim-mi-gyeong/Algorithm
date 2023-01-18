# 미네랄 2
from collections import deque
import sys

input = sys.stdin.readline

r, c = map(int, input().split())
graph = []
for i in range(r):
    tmp = list(input().rstrip())
    graph.append(tmp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()


def throw(turn, h):
    index_h = r - h

    target_x, target_y = index_h, -1

    if turn % 2 == 0:
        for j in range(c):
            if graph[index_h][j] == "x":
                target_y = j
                graph[index_h][j] = "."
                break
    else:
        for j in range(c - 1, -1, -1):
            if graph[index_h][j] == "x":
                target_y = j
                graph[index_h][j] = "."
                break

    for k in range(len(dx)):
        nx = target_x + dx[k]
        ny = target_y + dy[k]
        if 0 <= nx < r and 0 <= ny < c:
            if graph[nx][ny] == "x":
                queue.append((nx, ny))


def find_gravity_cluster(x, y):
    q = deque()
    visited = [[0] * c for _ in range(r)]
    gravity_list = []
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        if x == r - 1:
            return
        if graph[x + 1][y] == ".":
            gravity_list.append((x, y))
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and graph[nx][ny] == "x":
                visited[nx][ny] = 1
                q.append((nx, ny))

    gravity(visited, gravity_list)


def gravity(visited, gravity_list):
    fall_cnt, check = 1, False
    while True:
        for x, y in gravity_list:
            if x + fall_cnt == r - 1:
                check = True
                break
            if graph[x + fall_cnt + 1][y] == "x" and not visited[x + fall_cnt + 1][y]:
                check = True
                break

        if check:
            break

        fall_cnt += 1

    for i in range(r - 2, -1, -1):
        for j in range(c):
            if graph[i][j] == "x" and visited[i][j]:
                graph[i + fall_cnt][j] = "x"
                graph[i][j] = "."


n = int(input())
lst = list(map(int, input().rstrip().split()))
turn = 0
for i in range(n):
    h = lst[i]
    throw(turn, h)

    while queue:
        x, y = queue.popleft()
        find_gravity_cluster(x, y)

    turn += 1

for i in range(r):
    print(*graph[i], sep="")
