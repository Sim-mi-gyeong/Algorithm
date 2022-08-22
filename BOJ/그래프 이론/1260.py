# DFS 와 BFS

from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()


def dfs(start, visited):

    visited[start] = 1
    print(start, end=" ")

    for i in graph[start]:
        if not visited[i]:
            dfs(i, visited)


def bfs(start, visited):

    visited[start] = 1
    q = deque()
    q.append(start)

    while q:
        x = q.popleft()
        print(x, end=" ")
        for i in graph[x]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)


visited = [0] * (n + 1)
dfs(v, visited)

print()

visited = [0] * (n + 1)
bfs(v, visited)

