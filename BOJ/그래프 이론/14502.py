# 연구소

from collections import deque

n, m = map(int, input().split())  # 세로, 가로
lst = [list(map(int, input().split())) for _ in range(n)]
# 0: 빈칸, 1: 벽, 2: 바이러스
# 바이러스: 상하좌우 인접한 빈 공간으로 퍼져 나감
# 새로 세울 수 있는 벽의 수 = 3
# 안전영역 최대 크기
# 꽃길 문제랑 유사?

visited = [[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
virusCnt = 0


q = deque()

# 처음 바이러스가 2인 곳을 큐에 넣고 -> BFS
for i in range(n):
    for j in range(m):
        if lst[i][j] == 2:
            visited[i][j] = 1
            q.append((i, j))
            virusCnt += 1
            print("바이러스 (i, j) : ", (i, j))


def virus(lst):
    global virusCnt
    while q:
        x, y = q.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if lst[nx][ny] == 1:
                    visited[nx][ny] = 1
                    continue
                elif lst[nx][ny] == 0 and visited[nx][ny] == 1:
                    continue
                elif lst[nx][ny] == 0 and visited[nx][ny] != 1:
                    # lst[nx][ny] = 2
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    virusCnt += 1
                    print("바이러스 (nx, ny) : ", (nx, ny))

    return virusCnt


wallCnt = 0
maxSize = 0
for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
            visited[i][j] = 1
            wallCnt += 1


def bfs(cnt, wallCnt):
    global maxSize
    if cnt == 3:
        # 바이러스 전파
        virusCnt = virus(lst)
        size = n * m - virusCnt - wallCnt
        print("virusCnt : ", virusCnt, " wallCnt : ", wallCnt)
        maxSize = max(maxSize, size)

        return

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and lst[i][j] == 0:
                visited[i][j] = 1
                wallCnt += 1

                bfs(cnt + 1, wallCnt)

                # 벽 세우기 전으로 초기화(백트래킹)
                visited[i][j] = 0
                wallCnt -= 1


bfs(0, wallCnt)
print(maxSize)
