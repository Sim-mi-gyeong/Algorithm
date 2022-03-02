# 특정한 최단 경로
# 플로이드-워셜 : 시간초과

import sys
input = sys.stdin.readline
INF = int(1e9)
n, e = map(int, input().split())
start = 1
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j: graph[i][j] = 0

for _ in range(e):
    # 정점 a 에서 -> 정저 b로, 거리가 c
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

v1, v2 = map(int, input().split())

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = min(graph[1][v1] + graph[v1][v2] + graph[v2][n]
        , graph[1][v2] + graph[v2][v1] + graph[v1][n])
if ans >= INF: print(-1)
else: print(ans)