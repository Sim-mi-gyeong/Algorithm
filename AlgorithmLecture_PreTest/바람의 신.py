import sys
import copy

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def cal(graph):
    tmpVal = 0
    for i in range(n):
        for j in range(m):
            tmpVal = max(graph[i][j], tmpVal)
    return tmpVal


def dfs(cnt, graph):
    global maxVal
    if cnt == k:
        tmpVal = cal(graph)
        maxVal = max(maxVal, tmpVal)
        return

    for i in range(4):
        copyGraph = copy.deepcopy(graph)
        if i == 0:
            for col in range(m):
                for row in range(n):
                    if copyGraph[row][col] != 0:
                        if not (0 <= row + 1 < n):
                            continue
                        else:
                            copyGraph[row + 1][col] += copyGraph[row][col]
                            copyGraph[row][col] = 0
                            break

            dfs(cnt + 1, copyGraph)

        elif i == 1:
            for row in range(n):
                for col in range(m - 1, -1, -1):
                    if copyGraph[row][col] != 0:
                        if not (0 <= col - 1 < m):
                            continue
                        else:
                            copyGraph[row][col - 1] += copyGraph[row][col]
                            copyGraph[row][col] = 0
                            break

            dfs(cnt + 1, copyGraph)

        elif i == 2:
            for col in range(m):
                for row in range(n - 1, -1, -1):
                    if copyGraph[row][col] != 0:
                        if not (0 <= row - 1 < n):
                            continue
                        else:
                            sumVal = copyGraph[row][col]
                            copyGraph[row - 1][col] += sumVal
                            copyGraph[row][col] = 0
                            break

            dfs(cnt + 1, copyGraph)

        elif i == 3:
            for row in range(n):
                for col in range(m):
                    if copyGraph[row][col] != 0:
                        if not (0 <= col + 1 < m):
                            continue
                        else:
                            copyGraph[row][col + 1] += copyGraph[row][col]
                            copyGraph[row][col] = 0
                            break

            dfs(cnt + 1, copyGraph)


def solve():
    dfs(0, graph)
    ans = maxVal
    return ans


t = int(input())

for tc in range(1, t + 1):
    n, m, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    maxVal = 0
    ans = solve()
    print("#{} {}".format(tc, ans))
