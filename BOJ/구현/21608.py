# 상어 초등학교

import sys

input = sys.stdin.readline
n = int(input())
dic = dict()
for _ in range(n ** 2):
    num, s1, s2, s3, s4 = map(int, input().split())
    dic[num] = [s1, s2, s3, s4]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
graph = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]


def like(key):
    likeDic = dict()
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                likeCnt = 0
                for d in range(len(dx)):
                    ni = i + dx[d]
                    nj = j + dy[d]
                    if 0 <= ni < n and 0 <= nj < n:
                        if graph[ni][nj] in dic[key]:
                            likeCnt += 1
                likeDic[(i, j)] = likeCnt

    likeDic = dict(sorted(likeDic.items(), key=lambda x: x[1], reverse=True))
    return likeDic


def blank(tmpList):
    blankDic = dict()
    for tmp in tmpList:
        x, y = tmp[0], tmp[1]
        tmpblankCnt = 0
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    tmpblankCnt += 1
        blankDic[tmp] = tmpblankCnt

    blankDic = dict(sorted(blankDic.items(), key=lambda x: x[1], reverse=True))
    return blankDic


def solution():
    for key, val in dic.items():
        adjLikeDic = like(key)
        num2List = []
        maxTmpVal = max(adjLikeDic.values())
        for k, v in adjLikeDic.items():
            if v == maxTmpVal:
                num2List.append(k)
        if len(num2List) == 1:
            sx, sy = num2List[0][0], num2List[0][1]
            graph[sx][sy] = key
            visited[sx][sy] = 1
        else:
            blankDic = blank(num2List)
            maxBlankVal = max(blankDic.values())
            num3List = []
            for k, v in blankDic.items():
                if v == maxBlankVal:
                    num3List.append(k)
            num3List = sorted(num3List, key=lambda x: (x[0], x[1]))
            sx, sy = num3List[0][0], num3List[0][1]
            graph[sx][sy] = key
            visited[sx][sy] = 1


solution()


def satisfied():
    total = 0
    for i in range(n):
        for j in range(n):
            student = graph[i][j]
            tmpVal = 0
            for d in range(len(dx)):
                ni = i + dx[d]
                nj = j + dy[d]
                if 0 <= ni < n and 0 <= nj < n:
                    if graph[ni][nj] in dic[student]:
                        tmpVal += 1
            if tmpVal > 0:
                total += 10 ** (tmpVal - 1)
    return total


print(satisfied())
