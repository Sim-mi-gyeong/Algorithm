# 배열 돌리기2

import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
circleCnt = min(n, m) // 2
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def rotate():
    q = deque()

    for circle in range(circleCnt):
        x, y = circle, circle
        for dir in range(len(dx)):
            while True:
                nx = x + dx[dir]
                ny = y + dy[dir]
                if circle <= nx < n - circle and circle <= ny < m - circle:
                    q.append(graph[x][y])
                    x, y = nx, ny
                else:
                    break

        num = r % ((n - circle * 2) * 2 + (m - circle * 2) * 2 - 4)  # 각 변에 있는 칸의 개수 - 중복되는 칸의 개수
        for _ in range(num):
            q.appendleft(q.pop())

        for dir in range(len(dx)):
            while True:
                nx = x + dx[dir]
                ny = y + dy[dir]
                if circle <= nx < n - circle and circle <= ny < m - circle:
                    graph[x][y] = q.popleft()
                    x, y = nx, ny
                else:
                    break


rotate()
for i in range(n):
    print(*graph[i])
