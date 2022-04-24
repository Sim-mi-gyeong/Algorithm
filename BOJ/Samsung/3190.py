# 뱀
from collections import deque

n = int(input())
graph = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]

startX, startY = 0, 0
k = int(input())
for _ in range(k):
    i, j = map(int, input().split())
    graph[i - 1][j - 1] = 2

l = int(input())
dir = dict()
dirTime = []
for _ in range(l):
    x, c = input().split()
    dir[int(x)] = c
    dirTime.append(int(x))


time = 0
d = 0  # 현재 방향 동쪽
r = [0, 1, 2, 3]  # 동 - 남 - 서 - 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
length = 1
# 사과가 있어서 몸 길이를 늘렸다가 -> 다음 칸에 사과가 없으면?
tailX, tailY = startX, startY


def bfs(startX, startY, tailX, tailY):
    global time, length

    queue = deque()
    queue.append((startX, startY, tailX, tailY))
    d = 0
    while True:
        time += 1
        x, y, tailX, tailY = queue.popleft()
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == 1:
            breakX, breakY = nx, ny
            return time, breakX, breakY, graph[breakX][breakY]
        else:
            if graph[nx][ny] == 2:  # 사과가 위치한 경우, 방문 처리 & 몸 길이 늘리기
                graph[nx][ny] = 1
                length += 1
            else:  # 사과가 없는 경우, 길이가 1로 원상복구 되나? / 방문처리 -> 이전에 꼬리가 있는 경우는? 0으로 어떻게 ?
                # 머리 제외 전부 0으로 돌아가는가?
                graph[nx][ny] = 1
                graph[tailX][tailY] = 0  # 이동 전 꼬리 부분을 빈 칸으로
                tailX = tailX + dx[d]  # 꼬리 앞으로 당기기
                tailY = tailY + dy[d]

            if length > n:
                breakX, breakY = nx, ny
                return time, breakX, breakY

            queue.append((nx, ny, tailX, tailY))

        if time in dirTime:
            if dir[time] == "D":
                d = (d + 1) % 4
            elif dir[time] == "L":
                d = (d + 3) % 4


print(bfs(startX, startY, tailX, tailY))
