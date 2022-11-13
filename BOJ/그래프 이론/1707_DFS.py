# 이분 그래프 O(V+E)

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
k = int(input())


def dfs(graph, color, start, red):
    global check

    color[start] = red
    for i in graph[start]:
        if color[i] == red:
            check = False
            return
        if color[i] == 0:
            dfs(graph, color, i, -red)


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
            dfs(graph, color, i, 1)

    if check:
        print("YES")
    else:
        print("NO")
