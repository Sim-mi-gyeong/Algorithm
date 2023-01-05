# 특정 거리의 도시 찾기

import heapq
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

INF = int(1e9)


def dijstra(start):
    distance = [INF] * (n + 1)
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (distance[i[0]], i[0]))

    return distance


distance = dijstra(x)
result = []
for i in range(1, n + 1):
    if distance[i] == k:
        result.append(i)
if len(result) == 0:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)

