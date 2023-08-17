from collections import defaultdict


def solution(n, results):
    answer = 0
    win_graph = defaultdict(set)
    lose_graph = defaultdict(set)
    for winner, loser in results:
        win_graph[loser].add(winner)
        lose_graph[winner].add(loser)

    for i in range(1, n + 1):
        for winner in win_graph[i]:
            lose_graph[winner].update(lose_graph[i])
        for loser in lose_graph[i]:
            win_graph[loser].update(win_graph[i])

    for i in range(1, n + 1):
        if len(win_graph[i]) + len(lose_graph[i]) == n - 1:
            answer += 1

    return answer


def solution2(n, results):
    answer = 0

    graph = [[0] * n for _ in range(n)]

    for result in results:
        a, b = result[0], result[1]
        graph[a - 1][b - 1] = 1
        graph[b - 1][a - 1] = -1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                # 모르는 상태에서
                if graph[i][j] == 0:
                    if graph[i][k] == 1 and graph[k][j] == 1:
                        graph[i][j] = 1
                    elif graph[i][k] == -1 and graph[k][j] == -1:
                        graph[i][j] = -1

    # 순위가 결정되려면, 자신을 제외한 n-1 명의 선수와 겨루어야 함
    for i in range(n):
        if graph[i].count(0) == 1:
            answer += 1

    return answer
