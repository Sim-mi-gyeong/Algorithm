# 치즈

from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
q = deque()
graph = []
cnt = 0  # 치즈 개수
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j in range(m):
        if tmp[j] == 1:  # 치즈 : 1 / 빈칸 : 0
            cnt += 1
            # 초기 큐에 치즈 추가
            q.append((i, j))

visited = [[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 각 치즈 격자의 4변 중에서, 적어도 2변 이상이 실내 온도의 공기와 접촉한 경우 -> 한 시간만에 녹아 없어짐
# 각 치즈마다, 몇 개의 면이 공기와 접촉하는지 체크 ?

# 치즈 내부에 있는 공간은 치즈 외부 공기와 접촉하지 않음 -> 녹아 없어지지 않음

# 치즈 외부 공간 ?
# 치즈 내부 공간 ?

# 현재 치즈의 개수 넣기
# 큐에 있는 치즈들을 꺼내면서 -> 상하좌우 접촉 면수 개수 구해서 -> 접촉 면수 >= 2 인 경우 그대로 빼내고
# 접촉 면수 < 2 -> 다시 큐에 넣기

# 치즈 내부 공간은 어떻게 판단?
# 빈 공간 먼저 체크하자!!!
# 빈 공간이 상하좌우로 치즈에 덮혀있으면 -> 공기가 통하지 않음

# 그래프 각 격자가 다른 면과 인접한 칸 개수
copyGraph = graph[:]
time = 0


def bfs():
    global time

    while True:
        time += 1

        # 빈 공간 먼저 체크 -> 내부 공간
        for i in range(n):
            for j in range(m):
                tmpInner = 0
                if graph[i][j] == 0:
                    for k in range(len(dx)):
                        ni = i + dx[k]
                        nj = j + dy[k]
                        if 0 <= ni < n and 0 <= nj < m:
                            pass

        # 현재 큐에 들어있는 치즈의 개수만큼 탐색
        for _ in range(len(q)):
            x, y = q.popleft()
            tmpCnt = 0
            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    # 내부 공간이 아닌 외부 빈 공간인 경우 cnt + 1
                    if graph[nx][ny] == 0 and graph[nx][ny] != 2:
                        tmpCnt += 1

            # 녹지 않는 경우는 다시 큐에 치즈 추가하기
            if tmpCnt < 2:
                q.append((i, j))

        # 내부 공간 처리 부분 -> 일반 빈 공간으로 돌리기
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 2:
                    graph[i][j] = 0


bfs()
