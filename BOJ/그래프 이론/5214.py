# 환승
from collections import deque

n, k, m = map(int, input().split())
station = [[] for _ in range(n + 1)]
line = [[] for _ in range(m + 1)]  # 라인에 연결된 역
start, end = 1, n


def bfs(start, end, station, line):
    if start == end:
        return 1
    visitedStation = [0] * (n + 1)
    visitedLine = [0] * (m + 1)

    visitedStation[start] = 1
    q = deque()
    # 시작 역에 연결된 라인 방문 처리 및 큐에 추가
    for tmpLine in station[start]:
        visitedLine[tmpLine] = 1
        q.append((start, tmpLine))

    while q:
        currStation, currLine = q.popleft()

        for tmpStation in line[currLine]:
            # 라인에 존재하는 역 중에서 방문하지 않은 역에 대해
            if visitedStation[tmpStation] == 0:
                if tmpStation == end:
                    return visitedStation[currStation] + 1
                visitedStation[tmpStation] = visitedStation[currStation] + 1
                for adjLine in station[tmpStation]:
                    if not visitedLine[adjLine]:
                        visitedLine[adjLine] = 1
                        # 처음 시작한 역에 연결된 노선에 존재하는, 다른 역에 연결된 다른 노선에 대한 정보 추가
                        q.append((tmpStation, adjLine))

    return -1


for i in range(m):
    tmp = list(map(int, input().split()))
    for j in range(k):
        line[i + 1].append(tmp[j])
        station[tmp[j]].append(i + 1)


print(bfs(start, end, station, line))
