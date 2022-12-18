from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(startX, startY):
    # global n, m
    q = deque()
    init_visited = [[0] * m for _ in range(n)]
    # 경로를 추적할 그래프
    trackPath = [[0] * m for _ in range(n)]

    init_visited[startX][startY] = 1
    q.append((startX, startY, 0, list(), init_visited))

    while q:
        x, y, cnt, path, visited = q.popleft()
        print("(x, y, cnt, path) : ", (x, y, cnt, path))

        # 과자집에 도달할 때 이동 횟수
        if (x, y) == (n - 1, m - 1):
            print("도달 완료")
            print("cnt : ", cnt)
            return cnt, path

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # if not visited[nx][ny] and graph[nx][ny] == 1:
                if graph[nx][ny] == 1:
                    # visited[nx][ny] = 1
                    # (0, 0) 에서 (0, 1) 로 향하는 최소 이동 경로에서는, 다른 위치가 이미 방문처리 되어 있어서 방문을 하지 못하는 상태
                    q.append((nx, ny, cnt + 1, path + [(nx, ny)], visited))
                    # visited[nx][ny] = 0


minDist = 1e9


def checkDist(tmpCnt, tmpPath):
    global minDist
    dist = 0

    for x, y in bread:
        if (x, y) in tmpPath:
            continue
        print("까마귀가 먹을 부수러기 위치 : ", (x, y))
        dist += abs((r - 1) - x) + abs((c - 1) - y)  # 까마귀가 먹을 부스러기에서 시작 위치와 과자집 위치는 제외

    print("dist : ", dist)
    minDist = min(minDist, dist)

    return minDist


def solve():
    minCnt = 1e9
    minDist = 1e9
    # 이 cnt 가 최솟값일 때 + 까마귀가 먹는 빵 부스러기 거리 합 최소
    tmpCnt, tmpPath = bfs(0, 0)
    if tmpCnt <= minCnt:
        minCnt = tmpCnt
        minDist = checkDist(minCnt, tmpPath)
    return minCnt, minDist


t = int(input())

for tc in range(1, t + 1):
    n, m, r, c = map(int, input().split())  # (r, c) 는 (1, 1) 시작 기준 위치
    # graph = [list(map(int, input().split())) for _ in range(n)]  # 0 : X / 1 : 빵 부스러기 O
    graph = []
    bread = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        graph.append(tmp)
        for j in range(m):
            if tmp[j] == 1 and (i, j) != (0, 0) and (i, j) != (n - 1, m - 1):
                bread.append((i, j))

    ansTmp, ansDist = solve()
    print("#{} {} {}".format(tc, ansTmp, ansDist))


"""
1
4 4 2 1
1 1 1 1
1 1 1 0
1 0 1 1
1 0 1 1

"""

