from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(startX, startY):
    materialCnt = len(material)
    q = deque()
    visited = [[0] * m for _ in range(n)]

    visited[startX][startY] = 1
    q.append((startX, startY, 0))

    while q:
        x, y, time = q.popleft()
        if graph[x][y] == "0":
            materialCnt -= 1
            if materialCnt == 0:
                return time
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] != "#":
                visited[nx][ny] = 1
                q.append((nx, ny, time + 1))

    return -1


def solve():
    ans = 1e9
    for i in range(n):
        for j in range(m):
            if graph[i][j] != "#":
                startX, startY = i, j
                tmpVal = bfs(startX, startY)
                ans = min(ans, tmpVal)

    return ans


t = int(input())

for tc in range(1, t + 1):
    n, m, k = map(int, input().split())
    graph = [list(input()) for _ in range(n)]
    material = dict()
    for _ in range(k):
        r, c = map(int, input().split())
        graph[r - 1][c - 1] = "0"
        material[(r - 1, c - 1)] = 1
    ans = solve()
    print("#{} {}".format(tc, ans))
