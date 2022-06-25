from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(startX, startY, visited, graph, target):
    global minVal
    q = deque()
    q.append((startX, startY, 0, 0))
    visited[startX][startY][0] = 1

    while q:
        x, y, bit, dist = q.popleft()
        if dist < minVal:
            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][bit]:
                    visited[nx][ny][bit] = 1
                    ndist = dist + 1
                    # 엑스칼리버를 다 모은 경우
                    if bit + 1 == 1 << len(target):
                        # 목표 지점 도달
                        if graph[nx][ny] == "S":
                            minVal = min(minVal, ndist)
                        # 평지 혹은 산인 경우
                        else:
                            q.append((nx, ny, bit, ndist))

                    # 엑스칼리버를 다 모으지 못한 경우
                    if bit + 1 != 1 << len(target):
                        # 산인 경우 이동 불가
                        if graph[nx][ny] != "X":
                            # 엑스칼리버의 조각을 찾은 경우 -> 찾은 상태 반영
                            if graph[nx][ny] == "A" or graph[nx][ny] == "B" or graph[nx][ny] == "C":
                                targetNum = target.index((nx, ny))
                                nbit = bit | (1 << targetNum)
                                visited[nx][ny][nbit] = 1
                                q.append((nx, ny, nbit, ndist))
                            # 평지/왕궁인 경우 이동 가능
                            else:
                                q.append((nx, ny, bit, ndist))

    return minVal


t = int(input())
for tc in range(t):
    n, m, r, k = map(int, input().split())  # (r, k) : (시작 행, 열)
    startX, startY = r - 1, k - 1
    minVal = 1e9
    visited = [[[0 for _ in range(8)] for _ in range(m)] for _ in range(n)]
    graph = []
    target = []  # 엑스칼리버의 각 조각
    for i in range(n):
        tmp = list(input())
        for j in range(m):
            if tmp[j] == "A" or tmp[j] == "B" or tmp[j] == "C":
                target.append((i, j))
        graph.append(tmp)

    ans = bfs(startX, startY, visited, graph, target)
    print("#{}".format(tc + 1), ans)

