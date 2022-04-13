# 꽃길

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
num = 3
ans = 1e9
tmpSum = 0
dx, dy = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]
visited = [[0] * n for _ in range(n)]


def checkVisited(x, y):
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if visited[nx][ny] == 1:
            return False
    return True  # 5개 위치에 대해 전부 방문하지 않은 경우


def dfs(cnt):
    global ans, tmpSum
    if cnt == num:
        ans = min(ans, tmpSum)
        return

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if checkVisited(i, j):
                for k in range(len(dx)):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    tmpSum += lst[nx][ny]
                    visited[nx][ny] = 1

                dfs(cnt + 1)

                # 다음 재귀를 위해 초기화 -> 이전에 방문 처리를 헸던 지점에 대해 수행
                for k in range(len(dx)):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    tmpSum -= lst[nx][ny]
                    visited[nx][ny] = 0


dfs(0)
print(ans)
