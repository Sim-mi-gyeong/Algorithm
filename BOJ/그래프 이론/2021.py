# 최소 환승 경로

from collections import deque
import sys

input = sys.stdin.readline

n, l = map(int, input().split())
station = [list() for _ in range(n + 1)]
line = [list() for _ in range(l + 1)]
for i in range(l):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        if tmp[j] != -1:
            # 역에 연결되어 있는 라인
            station[tmp[j]].append(i + 1)
            # 라인에 연결되어 있는 역
            line[i + 1].append(tmp[j])

start, end = map(int, input().split())


def bfs(start, end):
    if start == end:
        return 0
    visitedStation = [-1] * (n + 1)  # 각 역까지 환승 횟수 저장 배열
    visitedLine = [0] * (l + 1)
    q = deque()
    visitedStation[start] = 0
    # 처음 시작 역에 연결되어 있는 각 라인을 큐에 추가 -> 이동(환승) 가능한 라인
    for tmpLine in station[start]:
        q.append((start, tmpLine))
        visitedLine[tmpLine] = 1
    while q:
        currStation, currLine = q.popleft()
        # 현재 라인에 연결된 각 역들에 대해
        for adjStation in line[currLine]:
            # 이미 방문하지 않은 역 중에서
            if visitedStation[adjStation] == -1:
                if adjStation == end:
                    # 도착 역의 환승 횟수 출력
                    return visitedStation[currStation]
                # adjStation 중에서 end 에 해당하는 역이 없는 경우, 다른 노선으로 환승해야 하므로 (환승 횟수 + 1)
                visitedStation[adjStation] = visitedStation[currStation] + 1
                # 현재 라인에 연결된 각 역들에 연결된, 각 라인을 큐에 추가 -> 현재 노선에서 도달할 수 있는 역에서, 다음으로 환승할 라인에 대해
                for adjLine in station[adjStation]:
                    if not visitedLine[adjLine]:
                        q.append((adjStation, adjLine))
    return -1


print(bfs(start, end))
