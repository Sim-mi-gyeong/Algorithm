import sys
import copy

input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

graph = [[[0] * 2 for _ in range(4)] for _ in range(4)]

fish = []
for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        graph[i][j // 2][j % 2] = tmp[j]

n = 4


def find_fish(graph, num):
    for i in range(n):
        for j in range(n):
            if graph[i][j][0] == num:
                return (i, j)

    return -1


def move_fish(graph, sharkX, sharkY):
    # 작은 번호부터 순서대로 8방향 중 한 방향으로 이동
    for num in range(1, 17):
        move_fish_pos = find_fish(graph, num)
        if move_fish_pos != -1:
            x, y = move_fish_pos[0], move_fish_pos[1]
            dir = graph[x][y][1]
            # 각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 [45도 반시계 회전]
            for _ in range(8):
                nx = x + dx[dir - 1]
                ny = y + dy[dir - 1]
                if 0 <= nx < n and 0 <= ny < n:
                    if not (nx == sharkX and ny == sharkY):
                        # 물고기의 이동 방향이 바뀐 경우, 물고기 간 위치를 바꾸어주기 전에 미리 반영해야 함
                        graph[x][y][1] = dir
                        graph[nx][ny][0], graph[x][y][0] = graph[x][y][0], graph[nx][ny][0]
                        graph[nx][ny][1], graph[x][y][1] = graph[x][y][1], graph[nx][ny][1]
                        break
                dir = (dir + 1) % 8


# 상어가 [현재 위치 + 현재 이동 방향 기준] 이동 가능한 위치 목록
def move_shark_loc(graph, sharkX, sharkY):
    # 상어의 현재 위치 기준 이동 가능한 위치 목록
    sharkDir = graph[sharkX][sharkY][1]
    sharkMoveEableList = []
    for i in range(1, 4):
        nextSharkX = sharkX + i * dx[sharkDir - 1]
        nextSharkY = sharkY + i * dy[sharkDir - 1]
        if 0 <= nextSharkX < n and 0 <= nextSharkY < n:
            # 상어는 물고기가 존재하는 위치로만 이동 가능
            if 1 <= graph[nextSharkX][nextSharkY][0] <= 16:
                sharkMoveEableList.append((nextSharkX, nextSharkY))

    return sharkMoveEableList


totalVal = 0
maxVal = 0

# totalVal 은 상어의 이동 위치에 따라 달라지는 값 -> 함수 내에서 파라미터 처리로 들고 다녀야 함
def dfs(graph, sharkX, sharkY, totalVal):
    global maxVal
    # graph 는 파라미터로 넘어온 최초 graph
    #  -> copyGraph 는 이전 상태를 저장하기 위한 graph -> 이후의 처리는 copyGraph 로
    copyGraph = copy.deepcopy(graph)
    # 상어나 물고기의 이동 방향은, 위치 정보만 있으면 알 수 있는 정보!
    tmpVal = copyGraph[sharkX][sharkY][0]
    totalVal += tmpVal  # 먹은 물고기 번호만큼 추가
    copyGraph[sharkX][sharkY][0] = -1  # 물고기가 잡아 먹힌 처리

    # 이동 후 이전 자리 빈 공간 처리 ?? 안 해도 되는가 ?? -> 상어의 위치를 저장하고, 실제 그래프 상의 그 칸은 -1 처리하여 빈칸으로 나타냄
    # graph[sharkX][sharkY][0], graph[sharkX][sharkY][1] = 0, 0

    # 물고기 이동
    move_fish(copyGraph, sharkX, sharkY)

    # 상어가 이동할 수 있는 목록 찾기
    sharkMoveEableList = move_shark_loc(copyGraph, sharkX, sharkY)
    if len(sharkMoveEableList) == 0:  # 상어가 이동할 수 있는 위치가 없는 경우 -> 귀가 -> 번호 합 도출
        maxVal = max(maxVal, totalVal)
        return

    # 상어 이동
    for nextSharkX, nextSharkY in sharkMoveEableList:
        dfs(copyGraph, nextSharkX, nextSharkY, totalVal)

    graph = copyGraph


dfs(graph, 0, 0, 0)
print(maxVal)
