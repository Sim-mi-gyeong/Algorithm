# 마법사 상어와 비바리기
import copy
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx_sub = [-1, 1, 1, -1]
dy_sub = [-1, -1, 1, 1]

cloud = [(n - 2, 0), (n - 2, 1), (n - 1, 0), (n - 1, 1)]
save_cloud = copy.deepcopy(cloud)
graph = [list(map(int, input().split())) for _ in range(n)]


def move_cloud(d, s):
    global cloud
    newCloud = []
    for c in cloud:
        x = c[0]
        y = c[1]
        for _ in range(s):
            x += dx[d - 1]
            y += dy[d - 1]
            if x < 0:
                x = n - 1
            elif x >= n:
                x = 0
            if y < 0:
                y = n - 1
            elif y >= n:
                y = 0
        newCloud.append((x, y))

    cloud = copy.deepcopy(newCloud)


def rainy():
    for c in cloud:
        x = c[0]
        y = c[1]
        graph[x][y] += 1


def miss_cloud():
    global cloud, save_cloud
    save_cloud = copy.deepcopy(cloud)
    cloud = []


def magic():
    for c in save_cloud:
        x = c[0]
        y = c[1]
        tmp = 0
        for i in range(len(dx_sub)):
            nx = x + dx_sub[i]
            ny = y + dy_sub[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > 0:
                    tmp += 1
        graph[x][y] += tmp


def make_new_cloud():
    global cloud
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 2:
                if (i, j) not in save_cloud:
                    cloud.append((i, j))
                    graph[i][j] -= 2


def sol(d, s):
    move_cloud(d, s)
    rainy()
    miss_cloud()
    magic()
    make_new_cloud()


for _ in range(m):
    d, s = map(int, input().split())
    sol(d, s)

total = 0
for i in range(n):
    for j in range(n):
        total += graph[i][j]

print(total)
