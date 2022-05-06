from collections import deque
from itertools import combinations


def solution(places):
    answer = []
    for place in places:
        graph = [[] * 5 for _ in range(5)]

        for i in range(len(place)):
            print("place[i] : ", place[i])
            for j in range(len(place[i])):
                graph[i].append(place[i][j])

        # 각 강의실(graph)마다 거리두기 확인하기 진행
        print(check(graph))
        if not check(graph):
            answer.append(0)
        else:
            answer.append(1)

    return answer


def check(graph):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    # 응시자 자리 사이의 거리가 2 초과인 경우 O
    # 응시자 자리 사이의 거리가 2 이하인 경우 파티션이 존재하는지 확인
    queue = deque()

    peopleList = []
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == "P":
                peopleList.append((i, j))

    if len(peopleList) == 0:
        # True
        ans = True
        return ans

    comPeople = list(combinations(peopleList, 2))

    for people in comPeople:
        # people : [(0, 0), (2, 0)]
        dist = abs(people[0][0] - people[1][0]) + abs(people[0][1] - people[1][1])
        if dist > 2:
            # 거리 조건 만족
            ans = True
        # 거리가 2 이하일때 -> 파티션 조건 확인
        else:
            # graph 에서 응시자 자리 사이에 빈칸 존재 여부 확인
            # P와 P 사이에서, X 가 있으면 True /  O가 있으면 False
            for i in range(len(graph)):
                for j in range(len(graph)):
                    x1, y1 = people[0][0], people[0][1]
                    x2, y2 = people[1][0], people[1][1]
                    for k in range(len(dx)):
                        nx = x1 + dx[k]
                        ny = y1 + dy[k]
                        if 0 <= nx < 5 and 0 <= ny < 5:
                            if graph[nx][ny] == "O":
                                for m in range(len(dx)):
                                    next_nx = nx + dx[m]
                                    next_ny = ny + dy[m]
                                    if 0 <= next_ny < 5 and 0 <= next_ny < 5:
                                        if (
                                            next_nx == x2
                                            and next_ny == y2
                                            and graph[next_nx][next_ny] == "P"
                                        ):
                                            ans = False

    return ans


print(
    solution(
        [
            ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
        ]
    )
)

