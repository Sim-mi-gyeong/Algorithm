# 아 맞다! 우산

from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())  # 가로, 세로

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
ans = 1e9
target = []
graph = []
visited = [[[0 for _ in range(32)] for _ in range(n)] for _ in range(m)]  # 물건 5개 -> 11111

for i in range(m):
    tmp = list(input().rstrip())
    for j in range(n):
        if tmp[j] == "S":
            startX, startY = i, j
        elif tmp[j] == "X":
            target.append((i, j))

    graph.append(tmp)


def bfs(startX, startY):
    global ans
    q = deque()
    q.append((startX, startY, 0, 0))  # 위치 행, 열, bit, 거리
    visited[startX][startY][0] = 1
    while q:
        x, y, bit, dist = q.popleft()
        # dist 가 현재 최솟값보다 큰 경우는 무시 가능
        if dist < ans:
            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny][bit]:
                    visited[nx][ny][bit] = 1
                    ndist = dist + 1
                    if graph[nx][ny] != "#":
                        # 탈출 지점 도달 및 물건을 모두 챙긴 상태인 경우
                        if graph[nx][ny] == "E" and bit + 1 == 1 << len(target):
                            ans = min(ans, ndist)
                        # 물건을 찾은 경우, 챙긴 상태 반영
                        elif graph[nx][ny] == "X":
                            targetNum = target.index((nx, ny))  # 해당 물건이 어떤 물건인지(몇 번 물건인지) 찾기
                            nbit = bit | (1 << targetNum)  # 해당 물건의 번호를 비트에 추가
                            visited[nx][ny][nbit] = 1
                            q.append((nx, ny, nbit, ndist))
                        else:
                            q.append((nx, ny, bit, ndist))


bfs(startX, startY)
print(ans)
