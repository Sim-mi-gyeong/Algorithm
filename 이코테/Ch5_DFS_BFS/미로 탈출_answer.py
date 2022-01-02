# 문제 해결 아이디어
# BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색
# 상, 하, 좌, 우로 연결된 모든 노드로의 거리가 1(동일)
# -> (1, 1) 지점부터 BFS를 수행해 모든 노드의 최단 거리 값을 기록해 해결
from collections import deque

# BFS 소스코드 구현
def bfs(x, y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]   # x 좌표를 행처럼
dy = [0, 0, -1, 1]   # y 좌표를 열처럼

# def bfs(x, y):
#     # queue = deque([graph[x][y]])
#     queue = deque()
#     queue.append(graph[x][y])

#     while queue:
#         v = queue.popleft()
#         for k in range(4):
#             x += dx[k]
#             y += dy[k]
#             if x < 0 or y < 0 or x >= n or y >= m:
#                 continue
#             if graph[x][y] == 0:
#                 continue
#             if graph[x][y] == 1:
#                 graph[x][y] = v + 1
#                 queue.append(graph[x][y])
#                 print(queue)

#     return graph[x][y]

#     # if graph[x][y] != 0:
#     #     # queue.append(graph[x][y])
#     #     v = queue.popleft()
        
print(bfs(0, 0))

