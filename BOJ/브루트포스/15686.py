# 치킨 배달

from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
path = [list(map(int, input().split())) for _ in range(n)]
lstHouse = []
lstChicken = []
for i in range(n):
    for j in range(n):
        if path[i][j] == 1: lstHouse.append((i, j))
        elif path[i][j] == 2: lstChicken.append((i, j))
INF = int(1e9)
minTotal = INF

tmpChickenList = list(combinations(lstChicken ,m))
for k in tmpChickenList:
    tmpTotal = 0 
    for i in range(len(lstHouse)):
        minTmpDist = INF
        for j in range(len(k)):
            tmpDist = abs(k[j][0] - lstHouse[i][0]) + abs(k[j][1] - lstHouse[i][1])
            if minTmpDist > tmpDist:
                minTmpDist = tmpDist
        tmpTotal += minTmpDist
    if minTotal > tmpTotal: minTotal = tmpTotal

print(minTotal)