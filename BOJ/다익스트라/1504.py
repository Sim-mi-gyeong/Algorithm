# 특정한 최단 경로

import heapq
import sys
input = sys.stdin.readline
# 정점의 개수, 간선의 개수
n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
for _ in range(e):
    # 정점 a 에서 -> 정점 b로 / 정점 b 에서 -> 정점 a 로, 거리가 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

start = 1
def dijkstra(start, end):
    q = []
    distance = [INF] * (n+1)
    distance[start] = 0
    heapq.heappush(q, (0, start))   # (거리, 노드)

    while q:
        dist, now = heapq.heappop(q)   # 현재 노드까지 거리, 현재 노드
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance[end]

v1, v2 = map(int, input().split())
cal1 = dijkstra(start, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
cal2 = dijkstra(start, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

check = max(cal1, cal2)
answer = min(cal1, cal2)
if check >= INF: print(-1)
else: print(answer)