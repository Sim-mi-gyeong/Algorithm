# 벽 / 빈 공간 / 목표 지점ㄴ
from collections import deque


def solution(places):
    answer = []
    for place in places:
        graph = [[] * 5 for _ in range(5)]

        for i in range(len(place)):
            for j in range(len(place[i])):
                graph[i].append(place[i][j])

        if not check(graph):
            answer.append(0)
        else:
            answer.append(1)

    return answer


def check(graph):
    ans = True
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    # 큐에 P의 위치를 전부 넣고 시작하는 것이 아닌, 한 개씩 넣고 시작
    p = []
    for i in range(5):
        for j in range(5):
            if graph[i][j] == "P":
                p.append((i, j))

    for subP in p:
        queue = deque([subP])
        visited = [[0] * 5 for _ in range(5)]
        distance = [[0] * 5 for _ in range(5)]
        visited[subP[0]][subP[1]] = 1

        # P 하나씩 담긴 큐로부터 반복 시작
        while queue:
            x, y = queue.popleft()

            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                    # O 인 경우에만 dist + 1 하면서 queue 에 넣고, 해당 graph 자리를 max(dist) 처리
                    if graph[nx][ny] == "O":
                        distance[nx][ny] = distance[x][y] + 1
                        visited[nx][ny] = 1
                        queue.append((nx, ny))

                    # X 는 벽 -> 이동 불가
                    elif graph[nx][ny] == "X":
                        continue

                    elif graph[nx][ny] == "P":
                        visited[nx][ny] = 1
                        distance[nx][ny] = distance[x][y] + 1
                        if distance[nx][ny] <= 2:
                            ans = False
                            return ans

                        # if distance[x][y] <= 1:
                        #     ans = False
                        #     return ans

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
