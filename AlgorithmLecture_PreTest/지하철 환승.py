from collections import deque


def bfs(start, end, station, line, visitedStation, visitedLine):
    if start == end:
        return 0

    q = deque()
    visitedStation[start] = 0
    for tmpLine in station[start]:
        visitedLine[tmpLine] = 1
        q.append((start, tmpLine))

    while q:
        currStation, currLine = q.popleft()

        for adjStation in line[currLine]:
            if visitedStation[adjStation] == -1:
                if adjStation == end:
                    return visitedStation[currStation]
                visitedStation[adjStation] = visitedStation[currStation] + 1
                for adjLine in station[adjStation]:
                    if not visitedLine[adjLine]:
                        q.append((adjStation, adjLine))

    return -1


t = int(input())
for tc in range(t):
    n, m, start, end = map(int, input().split())  # 지하철 역 수, 노선 수, 출발, 도착
    lst = map(int, input().split())  # 각 노선 별 역의 수
    station = [list() for _ in range(n + 1)]
    line = [list() for _ in range(m + 1)]
    visitedStation = [-1] * (n + 1)
    visitedLine = [0] * (m + 1)

    for i in range(m):
        tmp = list(map(int, input().split()))
        for j in range(len(tmp)):
            # 역에 연결되어 있는 라인
            station[tmp[j]].append(i + 1)
            # 라인에 연결되어 있는 역
            line[i + 1].append(tmp[j])

    ans = bfs(start, end, station, line, visitedStation, visitedLine)
    print("#{}".format(tc + 1), ans)
