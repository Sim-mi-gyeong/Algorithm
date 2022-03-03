# 최소 비용 구하기

import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    # a 에서 -> b로, c의 비용만큼
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())
INF = int(1e9)
distance = [INF] * (n+1)

def dijkstra(start, end):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)   # 현재 노드까지의 거리, 현재 노드
        if distance[now] < dist:   # 이미 방문한 노드
            continue
        for i in graph[now]:
            # dist, now = i[0], i[1]
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance[end]
# ans = dijkstra(start, end)
# if ans  INF: 
print(dijkstra(start, end))