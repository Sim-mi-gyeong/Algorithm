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

tree = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, age = map(int, input().split())
    tree[x - 1][y - 1].append(age)


def spring_and_summer():
    global tree, graph
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                tree[i][j].sort()
                dead_tree_age = 0
                live_tree_list = []

                for tmp_age in tree[i][j]:
                    if tmp_age > graph[i][j]:
                        dead_tree_age += tmp_age // 2
                    else:
                        graph[i][j] -= tmp_age
                        live_tree_list.append(tmp_age + 1)

                tree[i][j] = []
                tree[i][j].extend(live_tree_list)

                graph[i][j] += dead_tree_age


def fall_and_winter():
    global tree, graph
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                tree_num = len(tree[i][j])
                for k in range(tree_num):
                    if tree[i][j][k] % 5 != 0:
                        continue
                    for d in range(len(dx)):
                        ni = i + dx[d]
                        nj = j + dy[d]
                        if 0 <= ni < n and 0 <= nj < n:
                            tree[ni][nj].append(1)

            graph[i][j] += food[i][j]


def solve():
    spring_and_summer()
    fall_and_winter()


for _ in range(k):
    solve()

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(tree[i][j])

print(ans)
