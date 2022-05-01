# 미세먼지 안녕!

from copy import deepcopy

r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
newGraph = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(2)]


clear = []
for i in range(r):
    for j in range(c):
        # 3차원 그래프에 추가
        newGraph[0][i][j] = graph[i][j]
        if graph[i][j] == -1:
            clear.append((i, j))
clear.sort(key=lambda x: (x[0], x[1]))
clearUp, clearDown = clear[0], clear[1]

for a in range(t):
    print("t 가 ", a + 1, "일 때")
    # 미세먼지의 확산 Part - 모든 칸이 동시에 확산
    # -> 확산시킬 양들을 newGraph[1][i][j] 에 먼저 저장
    # -> newGraph[0][i][j] 의 각 칸들에 newGraph[1][i][j] 의 양들을 추가
    for i in range(r):
        for j in range(c):
            if newGraph[0][i][j] != 0 and newGraph[0][i][j] != -1:
                # 미세먼지가 있는 칸
                staub = newGraph[0][i][j]
                # 각 칸으로 확산될 먼지의 양
                staubDiv = staub // 5
                newGraph[1][i][j] = staubDiv

    # 먼지 확산
    for i in range(r):
        for j in range(c):
            if i != clearUp[0] and i != clearDown[0] and j != clearUp[1] and j != clearDown[1]:
                divCnt = 0
                for d in range(len(dx)):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    # 영역 밖 / 공기청정기 부분은 확산 X
                    if 0 <= nx < r and 0 <= ny < c and newGraph[0][nx][ny] != -1:
                        # graph[0][nx][ny] += staubDiv
                        newGraph[0][nx][ny] += newGraph[1][i][j]
                        divCnt += 1
                # 처음 미세먼지가 있던 칸에 남는 미세먼지
                newGraph[0][i][j] -= newGraph[1][i][j] * divCnt

    print("미세먼지 확산 후 ")
    print(newGraph)
    print()

    # 공기청정기 작동 Part -> newGraph[0] 부분에 작동
    for i in range(r):
        for j in range(c):
            # 공기청정기 작동 라인 제외
            # 공기청정기 부분은 고정
            # newGraph[1][clearUp[0]][clearUp[1]] = -1
            # newGraph[1][clearDown[0]][clearDown[1]] = -1

            if i != 0 and i != clearUp[0] and i != clearDown[0] and i != r - 1 and 1 <= j < c - 1:
                newGraph[1][i][j] = newGraph[0][i][j]
            # 공기청정기 윗 부분
            elif 0 <= i <= clearUp[0]:
                # 동쪽으로
                if i == clearUp[0] and 0 <= j < c - 1:
                    nx = i + dx[3]
                    ny = j + dy[3]
                    if newGraph[0][i][j] == -1:  # 만약, 공기청정기에서 나온 바람이라면, 0
                        newGraph[1][nx][ny] = 0
                    else:
                        newGraph[1][nx][ny] = newGraph[0][i][j]

                # 북쪽으로
                elif 0 < i <= clearUp[0] and j == c - 1:
                    nx = i + dx[0]
                    ny = j + dy[0]
                    newGraph[1][nx][ny] = newGraph[0][i][j]

                # 서쪽으로
                elif i == 0 and 1 <= j <= c - 1:
                    nx = i + dx[2]
                    ny = j + dy[2]
                    newGraph[1][nx][ny] = newGraph[0][i][j]

                # 남쪽으로
                elif 0 <= i < clearUp[0] - 1 and j == 0:
                    nx = i + dx[1]
                    ny = j + dy[1]
                    newGraph[1][nx][ny] = newGraph[0][i][j]

            # 공기청정기 아랫부분
            elif clearDown[0] <= i < r:
                # 동쪽으로
                if i == clearDown[0] and 0 <= j < c - 1:
                    nx = i + dx[3]
                    ny = j + dy[3]
                    if newGraph[0][i][j] == -1:  # 만약, 공기청정기에서 나온 바람이라면, 0
                        newGraph[1][nx][ny] = 0
                    else:
                        newGraph[1][nx][ny] = newGraph[0][i][j]

                # 남쪽으로
                elif clearDown[0] <= i < r - 1 and j == c - 1:
                    nx = i + dx[1]
                    ny = j + dy[1]
                    newGraph[1][nx][ny] = newGraph[0][i][j]

                # 서쪽으로
                elif i == r - 1 and 1 <= j <= c - 1:
                    nx = i + dx[2]
                    ny = j + dy[2]
                    newGraph[1][nx][ny] = newGraph[0][i][j]

                # 북쪽으로
                elif clearDown[0] - 1 < i <= r - 1 and j == 0:
                    nx = i + dx[0]
                    ny = j + dy[0]
                    newGraph[1][nx][ny] = newGraph[0][i][j]

            newGraph[1][clearUp[0]][clearUp[1]] = -1
            newGraph[1][clearDown[0]][clearDown[1]] = -1

    print("공기청정기 작동 후")
    print(newGraph[1])

    newGraph[0] = deepcopy(newGraph[1])
    # newGraph[1] 는 0값으로 초기화
    for i in range(r):
        for j in range(c):
            newGraph[1][i][j] = 0

    print(a + 1, " 초 지난 후")
    print(newGraph)
    print()

    # t 초 후 미세먼지의 양
    total = 0
    for i in range(r):
        for j in range(c):
            if newGraph[0][i][j] != -1:
                total += newGraph[0][i][j]

    print(total)
