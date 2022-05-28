from collections import deque

# # 0으로 붙어있는 아이스크림 개수 - 연결요소 개수 찾기
n, m = map(int, input().split())  # 세로, 가로
graph = [list(map(int, input())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[0] * m for _ in range(n)]
cnt = 0


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    queue.append([nx, ny])

    return True


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            if bfs(i, j):
                cnt += 1

print(cnt)

"""""" """""" """""" """"""

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

    return graph[n - 1][m - 1]


print(bfs(0, 0))
