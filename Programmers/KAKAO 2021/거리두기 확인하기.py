def solution(places):
    answer = []
    for place in places:
        graph = [[] * 5 for _ in range(5)]

        for i in range(len(place)):
            for j in range(len(place[i])):
                graph[i].append(place[i][j])

        # 각 강의실(graph)마다 거리두기 확인하기 진행
        if not check(graph):
            answer.append(0)
        else:
            answer.append(1)

    return answer


# 가능한 배치 상태 생각
def check(graph):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    ans = True

    for i in range(5):
        for j in range(5):
            if graph[i][j] == "O":
                cnt1 = 0
                for k in range(len(dx)):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if graph[nx][ny] == "P":
                            cnt1 += 1

                if cnt1 >= 2:
                    ans = False

            elif graph[i][j] == "P":
                cnt2 = 0
                for k in range(len(dx)):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if graph[nx][ny] == "P":
                            cnt2 += 1

                if cnt2 >= 1:
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

