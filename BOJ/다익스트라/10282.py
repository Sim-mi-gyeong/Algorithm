# 해킹

import sys
import heapq

input = sys.stdin.readline
t = int(input())

INF = int(1e9)


def dijkstra(start, graph):
    q = []
    distance = [INF] * (n + 1)
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    cnt = 0
    maxTime = 0
    for i in distance:
        if i != INF:
            cnt += 1
            maxTime = max(maxTime, i)

    return cnt, maxTime


for _ in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    parent = [i for i in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    cnt, time = dijkstra(c, graph)
    print(cnt, time)
