# 배열 돌리기 2

import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())  # n, m 크기 배열, r번 회전
graph = [list(map(int, input().split())) for _ in range(n)]
# 안쪽으로 갈수록, startX += 1 , endX -= 1
circleCnt = m // 2  # 돌려지는 라인 수
# startX, endX = 0, n - 1
# startY, endY = 0, m - 1
cnt = 0

# 아래쪽 오른쪽 위쪽 왼쪽
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
print("graph : ", graph)
while True:
    print(cnt + 1, " 회전 시작")
    if cnt > r:
        break

    # 회전을 위한 이전 그래프 복사
    new_graph = [g[:] for g in graph]
    # for i in graph:
    #     new_graph = graph[i][:]

    print("new_graph : ", new_graph)

    startX, endX = 0, n - 1
    startY, endY = 0, m - 1

    # 각 라인별로 회전
    for circle in range(circleCnt):
        print("")
        # startX, endX = 0, n - 1
        # startY, endY = 0, m - 1
        # 바깥쪽부터 -> 안쪽
        # dir = 0

        # while startX <= x < endX and startY <= y < endY:

        for dir in range(len(dx)):
            x, y = startX, startY
            nx, ny = x, y
            while startX <= nx < endX and startY <= ny < endY:
                print("(nx, ny) : ", (nx, ny))
                nx = x + dx[dir]
                ny = y + dy[dir]
                graph[nx][ny] = new_graph[x][y]
                # 옮겨야 할 위치 업데이트
                x, y = nx, ny

        # 한바퀴 돌고 안쪽 경계로
        startX += 1
        endX -= 1
        startY += 1
        endY -= 1

    cnt += 1

print(graph)
