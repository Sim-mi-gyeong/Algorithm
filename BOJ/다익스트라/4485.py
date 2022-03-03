# 녹색 옷 입은 애가 젤다지?

import heapq
import sys
input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
INF = int(1e9)
i = 1
while True:
    n = int(input()) 
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]

    def dijkstra(x, y):
        q = []
        distance[x][y] = graph[x][y]
        heapq.heappush(q, (distance[x][y], x, y))

        while q:
            dist, x, y = heapq.heappop(q) 
            
            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n:
                    if distance[nx][ny] < dist:
                        continue

                    cost = dist + graph[nx][ny]
                    if cost < distance[nx][ny]:
                        distance[nx][ny] = cost
                        heapq.heappush(q, (cost, nx, ny))

        return distance[n-1][n-1]

    total = dijkstra(0, 0)

    print(f'Problem {i}: {total}')
    i += 1