# 16236번 아기상어
from collections import deque
import sys

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n = int(input())
graph = []
fish = []
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j in range(n):
        if tmp[j] == 9:
            startX, startY = i, j
        elif 1 <= tmp[j] <= 6:
            fish.append((i, j, tmp[j]))

graph[startX][startY] = 0


def check_dist(currX, currY, currSize, targetX, targetY):
    q = deque()
    q.append((currX, currY, 0))
    visited = [[0] * n for _ in range(n)]
    visited[currX][currY] = 1

    while q:
        x, y, dist = q.popleft()
        if x == targetX and y == targetY:
            return dist
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] <= currSize:
                    q.append((nx, ny, dist + 1))
                    visited[nx][ny] = 1

    return int(1e9)


# 먹을 수 있는 물고기 체크
def check_enable(currX, currY, currSize):
    # 먹을 수 있는 물고기
    enable_fish_list = []
    for i, j, size in fish:
        # tmpDist = abs(currX - i) + abs(currY - j)
        tmpDist = check_dist(currX, currY, currSize, i, j)
        if currSize > size:
            enable_fish_list.append((i, j, size, tmpDist))

    enable_fish_list = sorted(enable_fish_list, key=lambda x: (x[3], x[0], x[1], x[2]))

    return enable_fish_list


# 가장 가까운 물고기 찾기
def shortest_fish(enable_fish_list):
    return enable_fish_list[0]


# 물고기를 먹으러 가기
def eat(currX, currY, currSize, currCnt, currTime, target):
    # 현재 위치부터 목표 위치까지 물고기를 먹기
    q = deque()
    q.append((currX, currY, currSize, currCnt, currTime))

    while q:
        x, y, currSize, currCnt, currTime = q.popleft()
        # 목표 지점에 도달한 경우
        if x == target[0] and y == target[1]:
            # 물고기를 먹은 자리 빈 공간 처리
            graph[x][y] = 0
            # 물고기를 먹을 수 있고 -> 현재까지 먹은 개수와 자신의 크기를 비교
            if currCnt + 1 == currSize:
                # 자신의 크기 + 1 / 먹은 개수 0 으로 초기화
                return x, y, currSize + 1, 0, currTime
            # 물고기를 먹을 수 있고 -> 현재까지 먹은 개수와 자신의 크기를 비교
            elif currCnt + 1 < currSize:
                return x, y, currSize, currCnt + 1, currTime

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # 다음 칸이 현재 자신의 크기보다 작은 경우 -> 지나갈 수 있음
                if graph[nx][ny] <= currSize:
                    q.append((nx, ny, currSize, currCnt, currTime + 1))


initSize = 2
eatCnt = 0
sharkSize = initSize
initTime = 0
totalTime = 0
while True:

    fish_list = check_enable(startX, startY, sharkSize)
    # 더 이상 먹을 수 있는 물고기가 없는 경우
    if len(fish_list) == 0:
        break
    target_fish = shortest_fish(fish_list)
    # 더 이상 도달할 수 있는 물고기가 없는 경우
    if target_fish[3] >= int(1e9):
        break
    target_fish = (target_fish[0], target_fish[1], target_fish[2])

    nx, ny, sharkSize, eatCnt, time = eat(startX, startY, sharkSize, eatCnt, 0, target_fish)
    startX, startY = nx, ny
    # time 은 한 개의 물고기를 먹으러 갈 때까지 걸린 시간
    totalTime += time

    # 먹은 물고기 제거
    fish.remove(target_fish)

print(totalTime)
