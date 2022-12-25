# 게리맨더링

from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline

n = int(input())
pepole = [0] + list(map(int, input().split()))
# graph = dict()
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    cnt, *line = map(int, input().split())
    for num in line:
        graph[i].append(num)


def bfs(regStart, reg):
    q = deque()
    visited = [0] * (len(reg) + 1)
    popSum, visitedNum = 0, 0

    visited[regStart] = 1
    q.append(regStart)
    popSum += pepole[regStart]
    visitedNum += 1

    while q:
        currReg = q.popleft()
        for i in reg[currReg]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)

                popSum += pepole[i]
                visitedNum += 1

    return popSum, visitedNum


ans = 1e9

for i in range(1, n // 2 + 1):
    # 1 ~ n // 2 까지
    for regA in list(combinations(range(1, n + 1), i)):
        regA = list(regA)
        popSumA, visitedNumA = bfs(regA[0], regA)

        regB = [j for j in range(1, n + 1) if not (j in regA)]
        popSumB, visitedNumB = bfs(regB[0], regB)

        if visitedNumA + visitedNumB == n:
            ans = min(ans, abs(popSumA - popSumB))
        print()

print(ans)
