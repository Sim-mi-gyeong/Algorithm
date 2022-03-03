# 알고스팟
# 0-1 너비 우선 탐색

import heapq

m, n = map(int, input().split())   # 가로, 세로
graph = [list(map(int, input())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
INF = int(1e9)
distance = [[INF] * m for _ in range(n)]

def dijkstra(x, y):
    q = []
    global cnt
    distance[x][y] = 0
    heapq.heappush(q, (distance[x][y], x, y))
    
    while q:
        dist, x, y = heapq.heappop(q)
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if distance[x][y] < dist:
                    continue
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (distance[nx][ny], nx, ny))
    
    return distance[n-1][m-1]

print(dijkstra(0, 0))