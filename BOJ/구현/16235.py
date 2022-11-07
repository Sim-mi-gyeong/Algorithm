# 나무 재테크
import sys

input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split())
graph = [[5] * n for _ in range(n)]

food = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    food.append(tmp)

tree_list = []
for _ in range(m):
    x, y, age = map(int, input().split())
    tree_list.append([x - 1, y - 1, age])


def spring():
    global tree_list, dead_tree_list

    # 나이가 적은 순으로 정렬
    tree_list = sorted(tree_list, key=lambda x: x[2])
    live_tree_list = []
    dead_tree_list = []
    for tree in tree_list:
        x, y, age = tree[0], tree[1], tree[2]
        if graph[x][y] < age:
            dead_tree_list.append([x, y, age])
            continue
        graph[x][y] -= age
        live_tree_list.append([x, y, age + 1])

    tree_list = live_tree_list


def summer():
    global graph, dead_tree_list
    for dead_tree in dead_tree_list:
        x, y, age = dead_tree[0], dead_tree[1], dead_tree[2]
        graph[x][y] += age // 2


def fall():
    global tree_list
    new_tree_list = tree_list
    for tree in tree_list:
        x, y, age = tree[0], tree[1], tree[2]
        if age % 5 != 0:
            continue
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                new_tree_list.append([nx, ny, 1])

    tree_list = new_tree_list


def winter():
    global graph
    for i in range(n):
        for j in range(n):
            graph[i][j] += food[i][j]


def solve():
    spring()
    summer()
    fall()
    winter()


for _ in range(k):
    solve()
print(len(tree_list))
