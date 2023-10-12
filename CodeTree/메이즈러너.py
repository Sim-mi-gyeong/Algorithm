import sys

input = sys.stdin.readline

# 정사각형 좌표 크기, 참가자 수, 게임 시간
n, m, k = map(int, input().split())


graph = [list(map(int, input().split())) for _ in range(n)]
part = dict()
completePart = dict()
for i in range(1, m + 1):
    x, y = map(int, input())
    x -= 1
    y -= 1
    part[i] = (x, y)
    completePart[i] = 0

targetX, targetY = map(int, input().split())
targetX -= 1
targetY -= 1

ansSum = 0
ansX, ansY = -1, -1


def isFinish():
    cnt = 0
    for key, val in completePart.items():
        if val == 1:
            cnt += 1

    return cnt == m


def check(num, x, y):
    if (x, y) == (targetX, targetY):
        completePart[num] = 1


def move(num, x, y):
    global ansSum
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for d in range(len(dx)):
        nx = x + dx[d]
        ny = y + dy[d]

        if not (0 <= nx < n and 0 <= ny < n):
            continue

        if graph[nx][ny] > 0:
            continue

        currDist = abs(x - targetX) + abs(y - targetY)
        nextDist = abs(nx - targetX) + abs(ny - targetY)

        if currDist < nextDist:
            continue

        part[num] = (nx, ny)
        ansSum += 1
        check(num, nx, ny)
        break


def rotate():
    pass


for tm in range(1, k + 1):
    if isFinish():
        break

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for key, val in part.items():
        if completePart[key]:
            continue
        move(key, val[0], val[1])

    rotate()
