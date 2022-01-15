# 안전 영역
# 높이가 4 이하인 지점 잠기고,
# 물에 잠긴 지역의 제외하고 [상하좌우]로만 이어진 구역 개수
import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    if land[x][y] == 1:
        land[x][y] = 0
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True

    return False

n = int(input())
path = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
ans = 1
cnt = 0

# 범위 정하기
ran = list()
for i in range(n):
    for j in range(n):
        if path[i][j] not in ran: ran.append(path[i][j])
ran.sort()

for h in ran:
    cnt = 0
    land = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if path[i][j] <= h:
                land[i][j] = 0   # 잠긴 경우
            else:
                land[i][j] = 1   # 잠기지 않는 경우
         
    for i in range(n):
        for j in range(n):
            if land[i][j] == 1:
                if dfs(i, j) == True: cnt += 1
    ans = max(ans, cnt)

print(ans)