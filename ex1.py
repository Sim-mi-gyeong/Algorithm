from collections import deque
import sys
import heapq

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n = int(input())
graph = []
fish = []
emptyCnt = 0
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j in range(n):
        if tmp[j] == 9:
            startX, startY = i, j
        elif tmp[j] == 0:
            emptyCnt += 1

# 물고기가 하나도 없는 경우(빈 공간 개수 = 전체 - 상어 개수) -> 0 출력 후 종료
zeroCnt = n * n - 1
if zeroCnt == emptyCnt:
    print(0)
    exit(0)

graph[startX][startY] = 0


def find_and_check(currX, currY, currSize):
    enable_fish_list = []
    q = deque()
    visited = [[0] * n for _ in range(n)]
    q.append((currX, currY, 0, currSize))
    visited[currX][currY] = 1

    while q:
        x, y, time, size = q.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 빈 공간 or 자신과 크기가 같은 물고기 -> 지나갈 수만 있음
                if graph[nx][ny] == 0 or graph[nx][ny] == currSize:
                    visited[nx][ny] = 1
                    q.append((nx, ny, time + 1, graph[nx][ny]))
                # 자신보다 크기가 작은 물고기 -> 먹을 수 있음
                elif graph[nx][ny] < currSize:
                    visited[nx][ny] = 1
                    q.append((nx, ny, time + 1, graph[nx][ny]))
                    # 거리 -> x좌표 -> y좌표 기준 정렬을 위한 최소 힙에 타겟 후보 물고기 추가
                    heapq.heappush(enable_fish_list, (time + 1, nx, ny, graph[nx][ny]))

    # 먹을 수 있는 물고기가 없는 겨우
    if len(enable_fish_list) == 0:
        return 0
    else:
        return enable_fish_list[0]


sharkSize = 2
totalTime = 0
eatCnt = 0
while True:

    target = find_and_check(startX, startY, sharkSize)
    # 먹을 수 있는 물고기가 없는 경우
    if not target:
        break

    targetTime, targetX, targetY, targetSize = target[0], target[1], target[2], target[3]

    totalTime += targetTime  # 시간 추가
    if eatCnt + 1 == sharkSize:  # 상어 크기 및 현재까지 먹은 물고기 수 처리
        sharkSize += 1
        eatCnt = 0
    else:
        eatCnt += 1
    # 먹은 물고기 자리 빈 공간 처리
    graph[targetX][targetY] = 0
    # 상어 이동 처리
    startX, startY = targetX, targetY

print(totalTime)
