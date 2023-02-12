# 전력난

import sys
import heapq

input = sys.stdin.readline


def solve():
    cnt = 0
    cost = 0
    while q:
        z, x, y = heapq.heappop(q)
        if find(x, parent) != find(y, parent):
            union(x, y)
            cnt += 1
            cost += z
        if cnt == n - 1:
            break
    ans = totalCost - cost
    return ans


def find(x, parent):
    if x == parent[x]:
        return parent[x]
    parent[x] = find(parent[x], parent)
    return parent[x]


def union(a, b):
    parentA = find(a, parent)
    parentB = find(b, parent)
    if parentA != parentB:
        parent[parentB] = parentA


while True:
    n, m = map(int, input().rstrip().split())
    if n == 0 and m == 0:
        break

    parent = [i for i in range(n + 1)]
    q = []
    totalCost = 0
    for _ in range(m):
        x, y, z = map(int, input().rstrip().split())
        totalCost += z
        heapq.heappush(q, (z, x, y))
    ans = solve()
    print(ans)
