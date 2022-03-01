# 문제 해결 아이디어
# 핵심 아이디어 : 한 도시에서 -> 다른 도시까지의 최단 거리 문제로 치환 가능
# N과 M의 범위가 충분히 크기 때문에 '우선순위 큐'를 활용한 '다익스트라 알고리즘' 구현 
# 노드의 개수 최대 30,000개 / 간선의 수 최대 200,000개
# 도달이 가능한 도시 중, 거리가 가장 먼 도시의 거리 출력

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

cnt = 0
maxDistance = 0
for d in distance:
    if d != INF:
        cnt += 1
        maxDistance = max(maxDistance, d)

# 시작 노드는 제외해야 하므로 cnt - 1
print(cnt-1, maxDistance)