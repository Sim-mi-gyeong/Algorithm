# 시간초과
from collections import deque

# S : 시작 위치
# . : 이동 가능한 칸
# X : 장에물

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(startX, startY, graph, k):
    cnt = 0
    q = deque()
    q.append((startX, startY, 0))

    while q:
        x, y, move = q.popleft()
        if move >= k:
            return cnt
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != "X":
                    q.append((nx, ny, move + 1))
            else:
                cnt += 1

    return 0


t = int(input())
for tc in range(t):
    n, m, k = map(int, input().split())  # 격자 행 수, 열 수, 이동 가능 횟수
    graph = []
    for i in range(n):
        tmp = list(input())
        for j in range(m):
            if tmp[j] == "S":
                startX, startY = i, j
        graph.append(tmp)
    ans = bfs(startX, startY, graph, k)
    print("#{}".format(tc + 1), ans % 1000000007)
