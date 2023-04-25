# 벽 부수고 이동하기 4

from collections import deque
import sys

input = sys.stdin.readline


n, m = map(int, input().split())
# graph = [list(input()) for _ in range(n)]
result = [[0] * m for _ in range(n)]
graph = []
for i in range(n):
    tmp = list(input())
    graph.append(tmp)
    for j in range(m):
        if tmp[j] == 0:
            result[i][j] = 0


# visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited = [[0] * m for _ in range(n)]

# 벽이 아닌, 빈 칸이면 -1 처리


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(startX, startY):
    global graph
    q = deque()
    # visited = [[0] * m for _ in range(n)]

    ### 실제로 그래프 상태를 변경하면 안 됨

    q.append((startX, startY))
    if graph[startX][startY] == 1:
        visited[startX][startY] += 1
    # 벽을 부수고

    while q:
        x, y = q.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    q.append((nx, ny))
                    # visited[nx][ny] = -1
                visited[nx][ny] += 1
                q.append((nx, ny))

                # if visited[nx][ny] == 0:
                #     # 방문 및 벽인지 체크
                #     # 벽이 아닌 경우 -> 방문처리 및 큐에만 추가
                #     if graph[nx][ny] == 0:
                #         q.append((nx, ny))
                #         # visited[nx][ny] = -1
                #     else:
                #         visited[nx][ny] += 1
                #         q.append((nx, ny))
                # graph[nx][ny] = 0   # 부수고
                # for j in range(4):

                #     nx2 = nx + dx[j]
                #     ny2 = ny + dy[j]
                #     if graph[nx2][ny2] == 0:
                #         visited[nx][ny] += 1


# check = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        print(visited[i][j], end="")
    print()
