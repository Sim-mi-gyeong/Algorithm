dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
startX, startY = 0, 0


def dfs(r, c, graph, x, y):
    global maxCnt, presentSet

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in presentSet:
            presentSet.add(graph[nx][ny])
            dfs(r, c, graph, nx, ny)
            presentSet.remove(graph[nx][ny])

    if maxCnt < len(presentSet):
        maxCnt = len(presentSet)
    return maxCnt


def solve(r, c, graph):
    global presentSet
    presentSet.add(graph[startX][startY])
    ans = dfs(r, c, graph, startX, startY)
    return ans


t = int(input())

for tc in range(t):
    r, c = map(int, input().split())
    graph = []
    presentSet = set()
    for i in range(r):
        tmp = list(input())
        graph.append(tmp)
    maxCnt = 0
    ans = solve(r, c, graph)
    print("#{}".format(tc + 1), ans)
