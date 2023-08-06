# 운동

import sys

input = sys.stdin.readline

v, e = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (v + 1) for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

ans = INF
for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            if graph[i][k] == INF or graph[k][j] == INF:
                continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


# 사이클 찾기
for i in range(1, v + 1):
    ans = min(ans, graph[i][i])

if ans == INF:
    print(-1)
else:
    print(ans)
