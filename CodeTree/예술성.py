from collections import deque


def reverse_rotate_90(graph):
    new_graph = list(map(list, zip(*graph)))[::-1]
    return new_graph


def rotate_90(graph):
    new_graph = list(map(list, zip(*graph[::-1])))
    return new_graph


def rotate_square():
    square_size = n // 2

    rec_range_x = [(0, n // 2 - 1), (0, n // 2 - 1), (n // 2 + 1, n - 1), (n // 2 + 1, n - 1)]
    rec_range_y = [(0, n // 2 - 1), (n // 2 + 1, n - 1), (0, n // 2 - 1), (n // 2 + 1, n - 1)]

    for i in range(4):
        tmp_graph = [[0] * square_size for _ in range(square_size)]
        startX, endX = rec_range_x[i][0], rec_range_x[i][1]
        startY, endY = rec_range_y[i][0], rec_range_y[i][1]
        for i in range(startX, endX + 1):
            for j in range(startY, endY + 1):
                tmp_graph[i - startX][j - startY] = graph[i][j]

        tmp_graph = rotate_90(tmp_graph)

        for i in range(startX, endX + 1):
            for j in range(startY, endY + 1):
                graph[i][j] = tmp_graph[i - startX][j - startY]


def rotate_cross():
    temp = graph[n // 2][:]

    for i in range(n):
        graph[n // 2][i] = graph[i][n // 2]

    for i in range(n):
        graph[i][n // 2] = temp[n - 1 - i]


def rotate():
    rotate_square()
    rotate_cross()


def addScore():
    # 2차원 그래프의 각 칸마다 4방향으로 탐색하면서, 다른 그룹인 경우 tmpVal 을 더하기
    # 이때, 1에서 -> 2로 / 2에서 -> 1로도 갈 수 있으므로 2로 나누어주기
    score = 0
    for i in range(n):
        for j in range(n):
            for d in range(len(dx)):
                ni = i + dx[d]
                nj = j + dy[d]
                # 다른 그룹인 경우
                if 0 <= ni < n and 0 <= nj < n and groupGraph[i][j] != groupGraph[ni][nj]:
                    groupANum = groupGraph[i][j]
                    groupBNum = groupGraph[ni][nj]

                    score += (
                        (groupInfo[groupANum][1] + groupInfo[groupBNum][1])
                        * (groupInfo[groupANum][0])
                        * (groupInfo[groupBNum][0])
                    )

    return score // 2


def bfs(startX, startY, groupNum):
    tmpCnt = 0
    q = deque()

    visited[startX][startY] = 1
    q.append((startX, startY, graph[startX][startY]))
    tmpCnt += 1
    groupGraph[startX][startY] = groupNum  # 각 칸의 그룹을 표시

    while q:
        x, y, num = q.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if num == graph[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny, graph[nx][ny]))
                    tmpCnt += 1
                    groupGraph[nx][ny] = groupNum

    return tmpCnt


def findGroup():
    global visited, groupGraph, groupInfo

    groupGraph = [[0] * n for _ in range(n)]
    groupInfo = dict()
    visited = [[0] * n for _ in range(n)]
    groupNum = 1

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                tmpCnt = bfs(i, j, groupNum)
                if groupNum not in groupInfo:
                    groupInfo[groupNum] = [graph[i][j], tmpCnt]
                    groupNum += 1


def solve():
    total = 0
    for _ in range(4):
        # 1. 그룹 찾기
        findGroup()
        # 2. 예술 점수 구하기
        total += addScore()
        # 3. 회전
        rotate()

    return total


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = solve()
print(ans)
