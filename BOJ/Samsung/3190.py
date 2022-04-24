# 뱀
from collections import deque

n = int(input())
graph = [[0] * n for _ in range(n)]
k = int(input())
for _ in range(k):
    i, j = map(int, input().split())
    graph[i - 1][j - 1] = 2

l = int(input())
dir = dict()
dirTime = []
for _ in range(l):
    x, c = input().split()
    dir[int(x)] = c
    dirTime.append(int(x))


time = 0
startX, startY = 0, 0
d = 0  # 현재 방향 동쪽
r = [0, 1, 2, 3]  # 동 - 남 - 서 - 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
length = 1


def bfs(x, y):
    global time, length
    graph[x][y] = 1
    moveQ = deque()
    moveQ.append((x, y))  # 뱀의 이동 위치
    d = 0

    while True:
        time += 1
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == 1:
            return time
        else:
            if graph[nx][ny] == 2:
                graph[nx][ny] = 1
                moveQ.append((nx, ny))
                length += 1
            elif graph[nx][ny] == 0:
                graph[nx][ny] = 1
                moveQ.append((nx, ny))

                tailX, tailY = moveQ.popleft()  # 가장 끝부분 꼬리 비우기
                graph[tailX][tailY] = 0

            if length > n:
                return time

            x, y = nx, ny

        if time in dirTime:
            if dir[time] == "D":
                d = (d + 1) % 4
            elif dir[time] == "L":
                d = (d + 3) % 4


print(bfs(startX, startY))
