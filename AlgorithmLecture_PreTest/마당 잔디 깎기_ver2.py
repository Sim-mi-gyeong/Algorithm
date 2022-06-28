import heapq


def solution(n, m, d, graph, lst):
    ans = 0

    for k in range(d):
        tmp = 0
        heap = []

        # 1일마다 잔디 자라기
        for i in range(n):
            for j in range(m):
                graph[i][j] += 1
                heapq.heappush(heap, (-graph[i][j], (i, j)))

        # lst 의 k 번만큼 heap 에서 빼내고, 값을 ans 에 추가 / 그 자리 위치를 1로
        for _ in range(lst[k]):
            popVal = heapq.heappop(heap)
            val, x, y = -(popVal[0]), popVal[1][0], popVal[1][1]
            tmp += val - 1
            graph[x][y] = 1
            heapq.heappush(heap, (-graph[x][y], (x, y)))

        ans += (k + 1) * tmp

    return ans


t = int(input())

for tc in range(t):
    n, m, d = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    lst = list(map(int, input().split()))
    ans = solution(n, m, d, graph, lst)
    print("#{}".format(tc + 1), ans)


"""
2
4 5 4
8 4 2 3 5
11 17 24 38 19
2 3 41 6 9
11 35 16 17 35
3 2 2 4
3 3 3
4 91 57
95 8 4
34 75 47
8 9 9

"""

