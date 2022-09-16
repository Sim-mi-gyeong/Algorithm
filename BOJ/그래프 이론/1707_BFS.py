# 이분 그래프 O(V+E)

import sys
from collections import deque

input = sys.stdin.readline
k = int(input())


def bfs(graph, color, start, red):
    global check
    q = deque()
    color[start] = red
    q.append((start, red))

    while q:
        v, col = q.popleft()  # 정점, 색깔
        for i in graph[v]:
            if color[i] == col:
                check = False
                return
            if color[i] == 0:
                color[i] = -col
                q.append((i, color[i]))


for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    color = [0] * (v + 1)
    check = True

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v + 1):
        if not check:
            break
        if color[i] == 0:
            bfs(graph, color, i, 1)

    if check:
        print("YES")
    else:
        print("NO")