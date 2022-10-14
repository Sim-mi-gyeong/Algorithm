### 배열 돌리기

print("----------- 정사각형 배열 -----------")
n = 5
graph = [[i * n + j for j in range(n)] for i in range(n)]
print("초기 그래프")
for row in graph:
    print(row)
print()


def rotate_90():
    new_graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_graph[i][j] = graph[n - j - 1][i]

    return new_graph


rotate_90_graph = rotate_90()
print("시계 방향 90도 회전 그래프")
for row in rotate_90_graph:
    print(row)
print()

print("----------- 직사각형 배열 -----------")
# (3, 4) 크기의 직사각형 2차원 배열
n = 3
m = 4
graph = [[i * m + j for j in range(m)] for i in range(n)]
print("초기 그래프")
for row in graph:
    print(row)
print()

# (1, 0) -> (0, 1) / (0, 0) -> (0, 2) / (0, 1) -> (1, 2)
def rotate_90(graph):
    n = len(graph)  # 행 길이 - 회전 전
    m = len(graph[0])  # 열 길이 - 회전 전
    new_graph = [[0] * n for _ in range(m)]
    # 회전 후의 행 번호 = 회전 전의 열 번호
    # 회전 후의 열 번호 = N - 1 - 회전 전의 행 번호
    for i in range(n):
        for j in range(m):
            new_graph[j][n - 1 - i] = graph[i][j]

    return new_graph


rotate_90_graph = rotate_90(graph)
print("시계 방향 90도 회전 그래프")
for row in rotate_90_graph:
    print(row)
print()


# (1, 0) -> (1, 2) / (0, 0) -> (2, 0) / (0, 1) -> (2, 1)
def rotate_180(graph):
    n = len(graph)
    m = len(graph[0])
    new_graph = [[0] * m for _ in range(n)]
    # 회전 후의 행 번호 = n - 1 - 회전 전의 행 번호
    # 회전 후의 열 번호 = m - 1 - 회전 전의 열 번호
    for i in range(n):
        for j in range(m):
            # new_graph[i][j] = graph[n-1-i][n-1-j]
            new_graph[n - 1 - i][m - 1 - j] = graph[i][j]
            # new_graph[m - j - 1][n - i - 1] = graph[i][j]

    return new_graph


rotate_180_graph = rotate_180(graph)
print("시계 방향 180도 회전 그래프")
for row in rotate_180_graph:
    print(row)
print()


# (1, 0) -> (2, 1) / (0, 0) -> (2, 0) / (0, 1) -> (1, 0)
def rotate_270(graph):
    n = len(graph)
    m = len(graph[0])
    new_graph = [[0] * n for _ in range(m)]
    # 회전 후의 행 번호 = N - 1 - 회전 전의 열 번호
    # 회전 후의 열 번호 = 회전 전의 행 번호
    for i in range(n):
        for j in range(m):
            # new_graph[i][j] = graph[n-1-j][i]
            # new_graph[n - 1 - j][i] = graph[i][j]
            new_graph[m - 1 - j][i] = graph[i][j]

    return new_graph


rotate_270_graph = rotate_270(graph)
print("시계 방향 270도 회전 그래프")
for row in rotate_270_graph:
    print(row)
print()


sample_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = [[], [], []]

for i in range(len(sample_list)):
    for j in range(len(sample_list[i])):
        new_list[i].append(sample_list[j][i])
print("배열 뒤집기 전 : ", sample_list)
print("배열 뒤집기 후 : ", new_list)

