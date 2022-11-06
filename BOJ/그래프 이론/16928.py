# 뱀과 사리 게임

from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [i for i in range(1, 101)]
bridge = dict()
snake = dict()
for _ in range(n):
    x, y = map(int, input().split())
    bridge[x] = y

for _ in range(m):
    x, y = map(int, input().split())
    snake[x] = y

num = [1, 2, 3, 4, 5, 6]


def bfs(start):
    q = deque()
    visited = [0] * 101
    q.append((start, 0))
    visited[start] = 1

    while q:
        x, cnt = q.popleft()
        if x == 100:
            return cnt
        for i in num:
            nx = x + i
            if nx in bridge:
                nx = bridge[nx]
                q.append((nx, cnt + 1))
            elif nx in snake:
                nx = snake[nx]
                q.append((nx, cnt + 1))
            else:
                if 0 <= nx <= 100 and not visited[nx]:
                    visited[nx] = 1
                    q.append((nx, cnt + 1))


print(bfs(1))
