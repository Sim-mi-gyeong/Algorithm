import sys

input = sys.stdin.readline

# 북풍(북 -> 남), 동풍(동 -> 서), 남풍(남 -> 북), 서풍(서 -> 동)
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

    # 북 / 동 / 남 / 서 풍 중에서
    for i in range(4):
        if i == 0:  # 북풍일 경우
            for col in range(m):
                for row in range(n):
                    if graph[row][col] != 0:
                        if not (0 <= row + 1 < n):
                            continue
                        else:
                            graph[row + 1][col] += graph[row][col]
                            graph[row][col] = 0
                            break
            dfs(cnt + 1, graph)

        elif i == 1:  # 동풍일 경우
            for row in range(n):
                for col in range(m - 1, -1):
                    if graph[row][col] != 0:
                        if not (0 <= col - 1 < m):
                            continue
                        else:
                            graph[row][col - 1] += graph[row][col]
                            graph[row][col] = 0
                            break
            dfs(cnt + 1, graph)
        elif i == 2:  # 남풍일 경우
            for col in range(m):
                for row in range(n - 1, -1):
                    if graph[row][col] != 0:
                        if not (0 <= row - 1 < n):
                            continue
                        else:
                            graph[row - 1][col] += graph[row][col]
                            graph[row][col] = 0
                            break
            dfs(cnt + 1, graph)
        elif i == 3:  # 서풍일 경우
            for row in range(n):
                for col in range(m):
                    if graph[row][col] != 0:
                        if not (0 <= col + 1 < m):
                            continue
                        else:
                            graph[row][col + 1] += graph[row][col]
                            graph[row][col] = 0
                            break
            dfs(cnt + 1, graph)


def solve():
    ans = 0

    return ans


t = int(input())

for tc in range(1, t + 1):
    n, m, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    maxVal = 0
    ans = solve()
    # solve()
    # ans = max
    print("#{} {}".format(tc, ans))
