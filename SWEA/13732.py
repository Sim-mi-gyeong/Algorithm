# 정사각형 판정


def bfs(graph):

    # 정사각형은, 왼쪽 위 / 왼쪽 아래 / 오른쪽 위 / 오른쪽 아래 좌표로 결정
    # 왼쪽 위 : x, y 좌표 최소 / 오른쪽 아래 : x, y 좌표 최대
    minMaxPos = [n, n, -1, -1]  # x 최소, y 최소, x 최대, y 최대
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "#":
                minMaxPos[0] = min(minMaxPos[0], i)
                minMaxPos[1] = min(minMaxPos[1], j)
                minMaxPos[2] = max(minMaxPos[2], i)
                minMaxPos[3] = max(minMaxPos[3], j)

    # 정사각형 변의 길이 확인
    width = minMaxPos[2] - minMaxPos[0] + 1
    height = minMaxPos[3] - minMaxPos[1] + 1

    if width != height:
        return False

    # 상하좌우 양 끝 위치가 나오면 -> 그 범위 내에서 탐색
    for i in range(minMaxPos[0], minMaxPos[2] + 1):
        for j in range(minMaxPos[1], minMaxPos[3] + 1):
            if graph[i][j] != "#":
                return False

    return True


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    graph = [[] for _ in range(n)]
    for i in range(n):
        s = input()
        for j in range(len(s)):
            graph[i].append(s[j])

    ans = bfs(graph)
    if ans:
        ans = "yes"
    else:
        ans = "no"
    print("#{} {}".format(test_case, ans))
