# 맥주 마시면서 걸어가기

from collections import deque
import sys

input = sys.stdin.readline

t = int(input())


def bfs(visited, startX, startY, endX, endY):
    q = deque()
    q.append((startX, startY))
    while q:
        x, y = q.popleft()
        if x == endX and y == endY:
            return "happy"
        for i in range(len(path)):
            nx = path[i][0]
            ny = path[i][1]
            if not visited[i]:
                if abs(nx - x) + abs(ny - y) <= 1000:
                    q.append((nx, ny))
                    visited[i] = 1
    return "sad"


for _ in range(t):
    n = int(input())
    startX, startY = map(int, input().split())
    path = []
    for _ in range(n):
        x, y = map(int, input().split())
        path.append((x, y))
    endX, endY = map(int, input().split())
    path.append((endX, endY))
    n, m = (endX - startX + 2), (endY - startY + 2)
    visited = [0] * len(path)
    print(bfs(visited, startX, startY, endX, endY))

# 전체를 다 방문할 경우 무조건 시간 초과
