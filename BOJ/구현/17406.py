import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
lst = []
for _ in range(k):
    r, c, s = map(int, input().split())
    lst.append((r - 1, c - 1, s))
perm_seq = list(permutations(lst, k))


def rotate(r, c, s):
    q = deque()
    startX, startY = r - s, c - s
    endX, endY = r + s, c + s
    row_size, col_size = endX - startX + 1, endY - startY + 1

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    circle_cnt = min(row_size, col_size) // 2
    for circle in range(circle_cnt):
        x, y = startX + circle, startY + circle

        for dir in range(len(dx)):
            while True:
                nx = x + dx[dir]
                ny = y + dy[dir]
                if (
                    startX + circle <= nx <= endX - circle
                    and startY + circle <= ny <= endY - circle
                ):
                    q.append(graph[x][y])
                    x, y = nx, ny
                else:
                    break

        q.appendleft(q.pop())

        for dir in range(len(dx)):
            while True:
                nx = x + dx[dir]
                ny = y + dy[dir]
                if (
                    startX + circle <= nx <= endX - circle
                    and startY + circle <= ny <= endY - circle
                ):
                    graph[x][y] = q.popleft()
                    x, y = nx, ny
                else:
                    break

    return graph


minVal = 1e9
for perm in perm_seq:

    new_graph = [[0] * m for _ in range(n)]
    for i in range(len(graph)):
        new_graph[i][:] = graph[i][:]

    for i in range(len(perm)):
        r, c, s = perm[i][0], perm[i][1], perm[i][2]
        graph = rotate(r, c, s)

    for i in range(len(graph)):
        minVal = min(minVal, sum(graph[i]))

    graph = [[0] * m for _ in range(n)]
    for i in range(len(new_graph)):
        graph[i][:] = new_graph[i][:]

print(minVal)
