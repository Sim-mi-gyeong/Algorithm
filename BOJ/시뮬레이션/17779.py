# 게리맨더링 2

import sys

input = sys.stdin.readline

n = int(input())
graph = [[0 for _ in range(n + 1)]]

totalPeople = 0
for i in range(1, n + 1):
    tmp = [0] + list(map(int, input().split()))
    graph.append(tmp)
    totalPeople += sum(tmp)


def solve(x, y, d1, d2):
    people = [0] * 5
    new_graph = [[0] * (n + 1) for _ in range(n + 1)]
    new_graph[x][y] = 5

    for i in range(1, d1 + 1):
        new_graph[x + i][y - i] = 5

    for i in range(1, d2 + 1):
        new_graph[x + i][y + i] = 5

    for i in range(1, d2 + 1):
        new_graph[x + d1 + i][y - d1 + i] = 5

    for i in range(1, d1 + 1):
        new_graph[x + d2 + i][y + d2 - i] = 5

    # 1번
    for i in range(1, x + d1):
        for j in range(1, y + 1):
            if new_graph[i][j] == 5:
                break
            else:
                people[0] += graph[i][j]

    # 2번
    for i in range(1, x + d2 + 1):
        for j in range(n, y, -1):
            if new_graph[i][j] == 5:
                break
            else:
                people[1] += graph[i][j]

    # 3번
    for i in range(x + d1, n + 1):
        for j in range(1, y - d1 + d2):
            if new_graph[i][j] == 5:
                break
            else:
                people[2] += graph[i][j]

    # 4번
    for i in range(x + d2 + 1, n + 1):
        for j in range(n, y - d1 + d2 - 1, -1):
            if new_graph[i][j] == 5:
                break
            else:
                people[3] += graph[i][j]

    # 5번
    people[4] = totalPeople - sum(people)
    return max(people), min(people)


ans = 1e9
for x in range(1, n + 1):
    for y in range(1, n + 1):
        for d1 in range(1, n + 1):
            for d2 in range(1, n + 1):
                if (1 <= x < x + d1 + d2 <= n) and (1 <= y - d1 < y < y + d2 <= n):
                    maxTmpPop, minTmpPop = solve(x, y, d1, d2)
                    ans = min(ans, abs(maxTmpPop - minTmpPop))

print(ans)
