# 문제 해결 아이디어
# 전형적인 최단 거리 문제 -> 최단 거리 알고리즘 이용
# N의 크기가 최대 100 -> 플로이드 워셜 알고리즘을 이용해도 효율적 해결 가능
# 플로이드 워셜 알고리즘 수행 후 -> (1번 노드 -> K 까지 최단 거리) + (K -> X까지 최단 거리)

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

x, k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
distance = graph[1][k] + graph[k][x]
if distance >= INF: print(-1)
else: print(distance)