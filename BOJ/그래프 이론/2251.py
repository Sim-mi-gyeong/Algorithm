# 물통

from collections import deque

a, b, c = map(int, input().split())
visited = [[[0] * (c + 1) for _ in range(b + 1)] for _ in range(a + 1)]
result = set()
q = deque()
q.append((0, 0, c))


def check(a, b, c):
    if not visited[a][b][c]:
        visited[a][b][c] = 1
        q.append((a, b, c))


def bfs():

    while q:
        tmpA, tmpB, tmpC = q.popleft()
        if tmpA == 0:
            result.add(tmpC)

        if tmpA > b - tmpB:
            check(tmpA - (b - tmpB), b, tmpC)
        else:
            check(0, tmpB + tmpA, tmpC)

        # a -> c
        if tmpA > c - tmpC:
            check(tmpA - (c - tmpC), tmpB, c)
        else:
            check(0, tmpB, tmpC + tmpA)

        # b -> a
        if tmpB > a - tmpA:
            check(a, tmpB - (a - tmpA), tmpC)
        else:
            check(tmpA + tmpB, 0, tmpC)

        # b -> c
        if tmpB > c - tmpC:
            check(tmpA, tmpB - (c - tmpC), c)
        else:
            check(tmpA, 0, tmpC + tmpB)

        # c -> a
        if tmpC > a - tmpA:
            check(a, tmpB, tmpC - (a - tmpA))
        else:
            check(tmpA + tmpC, tmpB, 0)

        # c -> b
        if tmpC > b - tmpB:
            check(tmpA, b, tmpC - (b - tmpB))
        else:
            check(tmpA, tmpB + tmpC, 0)


bfs()
result = sorted(list(result))
print(*result)
