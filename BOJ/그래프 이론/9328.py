# 열쇠

from collections import deque
import sys

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(startX, startY):
    q = deque()
    visited = [[0] * (w + 2) for _ in range(h + 2)]
    cnt = 0

    visited[startX][startY] = 1
    q.append((startX, startY))

    while q:
        x, y = q.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h + 2 and 0 <= ny < w + 2 and not visited[nx][ny]:
                if graph[nx][ny] == ".":
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                elif graph[nx][ny].isalpha() and graph[nx][ny].islower():
                    key[ord(graph[nx][ny]) - ord("a")] = 1
                    visited = [[0] * (w + 2) for _ in range(h + 2)]
                    graph[nx][ny] = "."
                    q.append((nx, ny))

                elif graph[nx][ny].isalpha() and graph[nx][ny].isupper():
                    if key[ord(graph[nx][ny]) - ord("A")]:
                        visited[nx][ny] = 1
                        graph[nx][ny] = "."
                        q.append((nx, ny))
                elif graph[nx][ny] == "$":
                    cnt += 1
                    visited[nx][ny] = 1
                    graph[nx][ny] = "."
                    q.append((nx, ny))

    return cnt


def padding():
    for tmp in graph:
        tmp.insert(0, ".")
        tmp.append(".")
    graph.insert(0, ["."] * (w + 2))
    graph.append(["."] * (w + 2))


t = int(input().rstrip())
for _ in range(t):
    h, w = map(int, input().rstrip().split())
    graph = [list(input().rstrip()) for _ in range(h)]
    key = [0] * 26

    keys = input().rstrip()
    for k in keys:
        if k != "0":
            key[ord(k) - ord("a")] = 1

    for i in range(h):
        for j in range(w):
            if graph[i][j].isalpha() and graph[i][j].isupper():
                if key[ord(graph[i][j]) - ord("A")]:
                    graph[i][j] = "."

    padding()
    ans = bfs(0, 0)
    print(ans)
