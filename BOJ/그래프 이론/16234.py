# 인구 이동

from collections import deque

n, l, r = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
check = False   # 연합 가능한 경우 존재 여부
cnt = 0   # 인구 이동 요일 수 

def bfs(x, y, p, visited):
    global check
    queue = deque([])
    visited[x][y] = 1
    queue.append([x, y])
    country = 1   # 연합에 속할 국가 수
    people = p[x][y]   # 연합에 속할 국가의 인구 수

    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:    # 현재 위치(x)에서 다음 위치(nx)로 방문한 적 없고,
                d = abs(p[x][y] - p[nx][ny])
                if l <= d <= r:
                    visited[nx][ny] = 1   # 방문처리 -> 국경 오픈 대상
                    queue.append([nx, ny])
                    country += 1
                    people += p[nx][ny]
    
    # 큐를 다 비우고, 인구 이동 처리
    if country > 1:
        for i in range(n):
            for j in range(n):
                if visited[i][j] == 1: 
                    p[i][j] = people // country
        check = True

while True:
    visited = [[0] * n for _ in range(n)]

    # 연합 체크 한 번
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:    
                bfs(i, j, p, visited)
            
    if not check:
        print(cnt)
        break

    cnt += 1
    check = False   # 초기화