# 경쟁적 전염
import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
virus = dict()
graph = []
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j in range(len(tmp)):
        if tmp[j] != 0 and tmp[j] not in virus:
            virus[tmp[j]] = (i, j)

s, targetX, targetY = map(int, input().split())
virus = dict(sorted(virus.items()))
visited = [[0] * n for _ in range(n)]


def bfs(graph, q, visited):
    while q:
        x, y, num, time = q.popleft()
        if time == s + 1:
            return graph[targetX - 1][targetY - 1]

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    graph[nx][ny] = num
                    q.append((nx, ny, graph[nx][ny], time + 1))

    return graph[targetX - 1][targetY - 1]


q = deque()
for key, val in virus.items():
    q.append((val[0], val[1], key, 1))
    visited[val[0]][val[1]] = 1

print(bfs(graph, q, visited))


"""
4 2
1 0 0 0
0 0 0 0
0 0 0 0
0 0 0 2
3 3 2

answer : 1
"""

