import sys

input = sys.stdin.readline

# 북풍(북 -> 남), 동풍(동 -> 서), 남풍(남 -> 북), 서풍(서 -> 동)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 그래프 각 칸 중 최댓값 찾기
def cal(graph):
    tmpVal = 0
    for i in range(n):
        for j in range(m):
            tmpVal = max(graph[i][j], tmpVal)

    return tmpVal


def dfs(cnt, graph):
    global maxVal
    if cnt == k:  # k 번의 바람 처리 후
        tmpVal = cal(graph)
        maxVal = max(maxVal, tmpVal)
        return

    # 북 / 동 / 남 / 서 풍 중에서
    # cnt 증가에 따라 이전 graph 상태 유지 필요 -> 재귀함수의 파라미터로 넘기기
    for i in range(4):
        if i == 0:  # 북풍일 경우
            # 가장 위의 행부터 -> 내려가면서, 값이 있는 경우 한 칸 아래로 밀기
            ### 각 열마다 자신의 열에서, 행을 내려가면서 확인해야 함
            for col in range(m):
                for row in range(n):
                    if graph[row][col] != 0:
                        # 한 칸 밀기, 이때 범위를 벗어나는지 체크
                        # 범위를 벗어나는 경우 -> 넘어가고
                        if not (0 <= row + 1 < n):
                            continue
                        else:
                            # 첫 번째 만나는 사람들을 바람의 진행 방향으로 한 칸 밀어낸다. -> 이후 pass
                            graph[row + 1][col] += graph[row][col]
                            graph[row][col] = 0
                            break
            dfs(cnt + 1, graph)

        elif i == 1:  # 동풍일 경우
            for row in range(n):
                for col in range(m - 1, -1):
                    if graph[row][col] != 0:
                        if not (0 <= col - 1 < m):
                            continue
                        else:
                            graph[row][col - 1] += graph[row][col]
                            graph[row][col] = 0
                            break
            dfs(cnt + 1, graph)
        elif i == 2:  # 남풍일 경우
            for col in range(m):
                for row in range(n - 1, -1):
                    if graph[row][col] != 0:
                        if not (0 <= row - 1 < n):
                            continue
                        else:
                            graph[row - 1][col] += graph[row][col]
                            graph[row][col] = 0
                            break
            dfs(cnt + 1, graph)
        elif i == 3:  # 서풍일 경우
            for row in range(n):
                for col in range(m):
                    if graph[row][col] != 0:
                        if not (0 <= col + 1 < m):
                            continue
                        else:
                            graph[row][col + 1] += graph[row][col]
                            graph[row][col] = 0
                            break
            dfs(cnt + 1, graph)


def solve():
    ans = 0

    return ans


t = int(input())

for tc in range(1, t + 1):
    n, m, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]  # 격자는 (행, 열) (1, 1) 부터 시작
    maxVal = 0
    ans = solve()
    # solve()
    # ans = max
    print("#{} {}".format(tc, ans))
