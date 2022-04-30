# 아기 상어

from collections import deque
import heapq

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

emptyCnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            startX, startY = i, j
            graph[i][j] = 0
        elif graph[i][j] == 0:
            emptyCnt += 1

if emptyCnt == n * n - 1:
    print(0)
    exit(0)

fishCnt = n * n - emptyCnt - 1
initSize = 2

# foodQ = []   # 거리, x위치, y위치, 물고기 크기


def findFood(startX, startY):
    visited = [[0] * n for _ in range(n)]
    foodQ = []  # 상어가 물고기를 먹을 때마다 다음 먹을 물고기 정보가 업데이트 되므로 함수 내에 선언
    q = deque()
    q.append((startX, startY, 0, initSize))  # x위치, y위치, 거리, 크기

    while q:
        x, y, dist, size = q.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # dist += 1   # 여기서 dist += 1 을 하면, 아래 if 조건 검사에 맞지 않은 경우도 +=1 되어 여러 번 더해짐
                if graph[nx][ny] == 0 or graph[nx][ny] == size:
                    # dist += 1
                    visited[nx][ny] = 1
                    q.append((nx, ny, dist + 1, size))
                elif 0 < graph[nx][ny] < size and not visited[nx][ny]:
                    # dist += 1   # 이렇게 함수 내에서 +1을 해주면, 목표값 기준으로 왼쪽/오른쪽까지의 거기가 같아야 하는데, 위의 for 문에서 한 번씩 움직일 때마다 중복으로 더해짐
                    heapq.heappush(foodQ, (dist + 1, nx, ny, graph[nx][ny]))
                    # 방문처리
                    visited[nx][ny] = 1
                    q.append((nx, ny, dist + 1, size))

    foodQ.sort(key=lambda x: (x[0], x[1], x[2]))

    return foodQ


# 현재 위치에서 목표의 각 지점까지를 찾아가며 목표 update
time = 0
eatCnt = 0
while fishCnt:
    food = findFood(startX, startY)
    if not food:
        break
    food = food[0]
    targetDist, targetX, targetY, targetSize = food[0], food[1], food[2], food[3]
    time += targetDist
    eatCnt += 1
    fishCnt -= 1
    if eatCnt == initSize:
        initSize += 1
        eatCnt = 0
    graph[targetX][targetY] = 0
    startX, startY = targetX, targetY

print(time)
