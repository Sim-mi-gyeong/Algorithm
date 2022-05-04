# 배열 돌리기 1 -> pypy3로도 시간초과
from copy import deepcopy  # 리스트 슬라이싱으로 복사하는 것이 더 빠름
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())  # 행, 열
graph = [list(map(int, input().split())) for _ in range(n)]

# 반시계 방향 : 남 -> 동 -> 북 -> 서
def rotate(graph):
    newGraph = [[0] * m for _ in range(n)]
    tmpN, tmpM = n, m
    start = 0

    while tmpM > int(m / 2):
        # 남쪽
        for i in range(start, tmpN - 1):
            newGraph[i + 1][start] = graph[i][start]

        # 동쪽으로
        for j in range(start, tmpM - 1):
            newGraph[tmpN - 1][j + 1] = graph[tmpN - 1][j]

        # 북쪽으로
        for i in range(start, tmpN - 1):
            newGraph[i][tmpM - 1] = graph[i + 1][tmpM - 1]

        # 서쪽으로
        for j in range(start, tmpM - 1):
            newGraph[start][j] = graph[start][j + 1]

        start += 1
        tmpM -= 1
        tmpN -= 1

    return newGraph


for _ in range(r):
    graph = deepcopy(rotate(graph))

for i in range(n):
    for j in range(m):
        print(graph[i][j], end=" ")
    print()
