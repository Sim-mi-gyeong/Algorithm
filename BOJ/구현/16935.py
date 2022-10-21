import sys

input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
lst = list(map(int, input().split()))


def reverse_up_down(graph):
    row, col = len(graph), len(graph[0])
    new_graph = [[0] * col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            new_graph[row - i - 1][j] = graph[i][j]
    return new_graph


def reverse_left_right(graph):
    row, col = len(graph), len(graph[0])
    new_graph = [[0] * col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            new_graph[i][col - j - 1] = graph[i][j]
    return new_graph


def rotate_90(graph):
    new_graph = list(map(list, zip(*graph[::-1])))
    return new_graph


def rotate_reverse_90(graph):
    new_graph = list(map(list, zip(*graph)))[::-1]
    return new_graph


def group_rotate(graph):
    row, col = len(graph), len(graph[0])
    new_graph = [[0] * col for _ in range(row)]
    n_size, m_size = row // 2, col // 2

    targetX = [(0, n_size), (0, n_size), (n_size, row), (n_size, row)]
    targetY = [(0, m_size), (m_size, col), (m_size, col), (0, m_size)]

    for k in range(4):
        for i in range(targetX[k][0], targetX[k][1]):
            for j in range(targetY[k][0], targetY[k][1]):
                if k == 0:
                    new_graph[i][j + m_size] = graph[i][j]
                elif k == 1:
                    new_graph[i + n_size][j] = graph[i][j]
                elif k == 2:
                    new_graph[i][j - m_size] = graph[i][j]
                else:
                    new_graph[i - n_size][j] = graph[i][j]
    return new_graph


def group_rotate_reverse(graph):
    row, col = len(graph), len(graph[0])
    new_graph = [[0] * col for _ in range(row)]
    n_size, m_size = row // 2, col // 2

    targetX = [(0, n_size), (n_size, row), (n_size, row), (0, n_size)]
    targetY = [(0, m_size), (0, m_size), (m_size, col), (m_size, col)]

    for k in range(4):
        for i in range(targetX[k][0], targetX[k][1]):
            for j in range(targetY[k][0], targetY[k][1]):
                if k == 0:
                    new_graph[i + n_size][j] = graph[i][j]
                if k == 1:
                    new_graph[i][j + m_size] = graph[i][j]
                if k == 2:
                    new_graph[i - n_size][j] = graph[i][j]
                else:
                    new_graph[i][j - m_size] = graph[i][j]
    return new_graph


for cal in lst:
    if cal == 1:
        graph = reverse_up_down(graph)
    elif cal == 2:
        graph = reverse_left_right(graph)
    elif cal == 3:
        graph = rotate_90(graph)
    elif cal == 4:
        graph = rotate_reverse_90(graph)
    elif cal == 5:
        graph = group_rotate(graph)
    else:
        graph = group_rotate_reverse(graph)

for i in range(len(graph)):
    print(*graph[i])
