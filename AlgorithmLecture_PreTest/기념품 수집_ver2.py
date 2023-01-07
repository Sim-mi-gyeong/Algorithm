from collections import deque, defaultdict


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
startX, startY = 0, 0


def bfs(r, c, graph, present):
    maxCnt = 0
    q = deque()
    visited = [[0] * c for _ in range(r)]
    presentSet = set()

    visited[startX][startY] = 1
    q.append((startY, startY))
    presentSet.add(graph[startX][startY])

    while q:
        x, y = q.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if graph[nx][ny] not in presentSet:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    presentSet.add(graph[nx][ny])

    print("len(presentSet : ", len(presentSet))

    maxCnt = max(maxCnt, len(presentSet))
    return maxCnt


def solve(r, c, graph, present):
    ans = 0
    ans = bfs(r, c, graph, present)
    return ans


t = int(input())

for tc in range(t):
    r, c = map(int, input().split())
    graph = []
    present = defaultdict(list)

    for i in range(r):
        tmp = list(input())
        graph.append(tmp)
        for j in range(c):
            present[tmp[j]].append((i, j))

    ans = solve(r, c, graph, present)
    print("#{}".format(tc + 1), ans)
