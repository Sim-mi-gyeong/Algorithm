# 회사의 개수, 경로의 개수
import sys
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b: graph[a][b] = 0
        
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1): 
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
# 1번 회사에서 출발 -> k 방문 -> x 도착
x, k = map(int, input().split())
if graph[1][k] + graph[k][x] >= INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])