# 배열 돌리기 6
import sys

input = sys.stdin.readline
N, R = map(int, input().split())
n = 2 ** N
graph = [list(map(int, input().split())) for _ in range(n)]


def reverse_up_down(graph):
    row, col = len(graph), len(graph[0])
    new_graph = [[0] * col for _ in range(row)]

    for i in range(row):
        for j in range(col):
            new_graph[row - 1 - i][j] = graph[i][j]

    return new_graph


def reverse_left_right(graph):
    row, col = len(graph), len(graph[0])
    new_graph = []

    for i in range(row):
        for j in range(col):
            new_graph[i][col - 1 - j] = graph[i][j]

    return new_graph


def rotate_90(graph):
    return list(map(list, zip(*graph[::-1])))


def rotate_reverse_90(graph):
    return list(map(list, zip(*graph)))[::-1]


def cal_1(graph, l):
    size = 2 ** l
    new_graph = [[0] * n for _ in range(n)]

    cnt = n // size
    tmp_graph = [[0] * size for _ in range(size)]
    startX, endX = 0, size
    startY, endY = 0, size
    for _ in range(cnt):
        for i in range(startX, endX):
            for _ in range(cnt):
                for j in range(startY, endY):
                    tmp_graph[startX - i][startY - j] = graph[i][j]

                    new_tmp_graph = reverse_up_down(tmp_graph)

                    new_graph[startX + i][startY + j] = new_tmp_graph[i][j]

                startY = endY
                endY += size

        startX = endX
        endX += size

    return new_graph


def cal_2(graph, l):
    size = 2 ** l
    new_graph = [[0] * n for _ in range(n)]
    cnt = n // size

    tmp_graph = [[0] * size for _ in range(size)]

    startX, endX = 0, size
    startY, endY = 0, size

    for _ in range(cnt):
        for i in range(startX, endX):
            for _ in range(cnt):
                for j in range(startY, endY):
                    tmp_graph[startX - i][startY - j] = graph[i][j]

                    new_tmp_graph = reverse_left_right(tmp_graph)

                    new_graph[startX + i][startY + j] = new_tmp_graph[i][j]

                startY = endY
                endY += size

        startX = endX
        endX += size

    return new_graph


def cal_3(graph, l):
    size = 2 ** l
    new_graph = []

    return new_graph


def cal_4(graph, l):
    size = 2 ** l
    new_graph = []

    return new_graph


def cal_5(graph, l):
    size = 2 ** l
    new_graph = []

    return new_graph


def cal_6(graph, l):
    size = 2 ** l
    new_graph = []

    return new_graph


def cal_7(graph, l):
    size = 2 ** l
    new_graph = []

    return new_graph


def cal_8(graph, l):
    size = 2 ** l
    new_graph = []

    return new_graph


for _ in range(R):
    k, l = map(int, input().split())
    cal_dict = {
        1: cal_1(graph, l),
        2: cal_2(graph, l),
        3: cal_3(graph, l),
        4: cal_4(graph, l),
        5: cal_5(graph, l),
        6: cal_6(graph, l),
        7: cal_7(graph, l),
        8: cal_8(graph, l),
    }

    graph = cal_dict[k]


for i in range(len(graph)):
    print(*graph[i])
