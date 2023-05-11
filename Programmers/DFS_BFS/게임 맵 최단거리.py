from collections import deque


def solution(maps):
    answer = -1
    n, m = len(maps), len(maps[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    q.append((0, 0, 1))

    while q:
        x, y, cnt = q.popleft()
        if (x, y) == (n - 1, m - 1):
            answer = cnt
            break
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = 1
                q.append((nx, ny, cnt + 1))

    return answer


print(
    solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]])
)
print(
    solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]])
)

