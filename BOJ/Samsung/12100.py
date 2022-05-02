# 2048(Easy)

from itertools import permutations

n = int(input())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

graph = [list(map(int, input().split())) for _ in range(n)]
num = 5
dir = ["up", "down", "right", "left"]
lst = list(permutations(dir, num))
print(lst)

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, graph[i][j])
print(ans)
