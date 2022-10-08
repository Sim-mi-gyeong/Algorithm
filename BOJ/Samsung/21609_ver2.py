# 상어 중학교

from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def find_group(startX, startY, blockNum):
    q = deque()
    q.append((startX, startY))  # 처음 블록 = 기준 블록 = 색상 고정
    visited[startX][startY] = 1

    normal_block = [(startX, startY)]
    rainbow_block = []

    while q:
        x, y = q.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 무지개 블록을 만난 경우
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    rainbow_block.append((nx, ny))

                # 일반 블록을 만난 경우 - 기준 블록의 색상
                elif graph[nx][ny] == blockNum:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    normal_block.append((nx, ny))

    # 무지개 블록 방문 철회
    for x, y in rainbow_block:
        visited[x][y] = 0

    # 그룹 내 전체 블록 수, 무지개 블록 수, 그룹 내 블록 위치 정보
    blockCnt = len(normal_block) + len(rainbow_block)
    tmpGroup = normal_block + rainbow_block
    return blockCnt, len(rainbow_block), tmpGroup


def set_empty_get_point(groupBlocks):
    global total

    for i, j in groupBlocks:
        graph[i][j] = -2

    total += len(groupBlocks) ** 2


def gravity(graph):
    for i in range(n - 2, -1, -1):
        for j in range(n):
            if graph[i][j] != -1:
                tmp = i
                while 0 <= tmp + 1 < n and graph[tmp + 1][j] == -2:
                    graph[tmp + 1][j] = graph[tmp][j]
                    graph[tmp][j] = -2
                    tmp += 1

    return graph


def reverse_rotate_90(graph):
    n = len(graph)
    m = len(graph[0])
    newGraph = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            newGraph[m - 1 - j][i] = graph[i][j]

    return newGraph


total = 0
while True:
    group = []
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and 1 <= graph[i][j] <= m:
                blockCnt, rainbowCnt, tmpGroup = find_group(i, j, graph[i][j])
                if blockCnt >= 2:  # 블록의 개수 >= 2 인 경우 그룹 가능
                    group.append((blockCnt, rainbowCnt, tmpGroup))

    # 후보 그룹이 하나도 없다면 종료
    if len(group) < 1:
        break

    # 기준 블록에 대한 정보를 저장하지 않았지만 -> 정렬 조건이 전체 내림차순 정렬
    group = sorted(group, reverse=True)
    targetGroup = group[0]
    groupBlocks = targetGroup[2]
    set_empty_get_point(groupBlocks)

    graph = gravity(graph)

    graph = reverse_rotate_90(graph)

    graph = gravity(graph)

print(total)
