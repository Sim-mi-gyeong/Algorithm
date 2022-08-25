# 숨바꼭질 2

from collections import deque

n, k = map(int, input().split())

cnt = 0
visited = [[0, 0] for _ in range(100001)]


def bfs(start, visited):
    global cnt
    q = deque()
    visited[start][1] = 1
    q.append(start)

    while q:
        x = q.popleft()
        dx = [x - 1, x + 1, 2 * x]
        for i in range(len(dx)):
            nx = dx[i]

            if 0 <= nx <= 100000:
                if visited[nx][1] == 0:
                    visited[nx][0] = visited[x][0] + 1
                    visited[nx][1] = visited[x][1]
                    q.append(nx)

                elif visited[nx][0] == visited[x][0] + 1:  # 시간이 1초 더 걸리는 위치라면,
                    visited[nx][1] += visited[x][
                        1
                    ]  # 처음 목표 지점까지 도달한 최소 시간의 경우의 수 + 이 목표지점 이전 위치까지 도달한 최소 시간의 경우의 수


bfs(n, visited)
print(visited[k][0], visited[k][1])
