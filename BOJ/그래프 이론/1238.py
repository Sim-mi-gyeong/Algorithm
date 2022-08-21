# 파티
import heapq
import sys

input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end, time = map(int, input().split())
    graph[start].append((end, time))

INF = int(1e9)


def dijkstra(start, end):
    d = [INF] * (n + 1)
    q = []
    d[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if d[now] < dist:
            continue
        for i in graph[now]:
            distance = dist + i[1]
            if distance < d[i[0]]:
                d[i[0]] = distance
                heapq.heappush(q, (distance, i[0]))

    return d[end]


maxVal = 0
for num in range(1, n + 1):
    tmp = dijkstra(num, x) + dijkstra(x, num)
    maxVal = max(maxVal, tmp)
print(maxVal)
