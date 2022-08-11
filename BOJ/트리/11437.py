# LCA

import sys

sys.setrecursionlimit(100000)

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

d = [0] * (n + 1)
visited = [0] * (n + 1)
parent = [0] * (n + 1)


def dfs(x, depth):
    visited[x] = True
    d[x] = depth

    for y in graph[x]:
        if visited[y]:
            continue
        parent[y] = x
        dfs(y, depth + 1)


def lca(a, b):
    # 깊이가 같아질 때까지
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]

    # 노드가 같아질 때까지
    while a != b:
        a = parent[a]
        b = parent[b]

    return a


dfs(1, 0)  # 루트 노드 초기화

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
