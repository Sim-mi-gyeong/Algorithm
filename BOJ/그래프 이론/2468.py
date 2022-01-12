# 안전 영역
# 높이가 4 이하인 지점 잠기고,
# 물에 잠긴 지역의 제외하고 [상하좌우]로만 이어진 구역 개수
import sys
sys.setrecursionlimit(100000)

n = int(input())
path = [list(map(int, input().split())) for _ in range(n)]
copy_path = path.copy()
print(copy_path)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
ans = 0
cnt = 0
# 범위 정하기
ran = list()
for i in range(n):
    for j in range(n):
        if path[i][j] not in ran: ran.append(path[i][j])
ran.sort()

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    # if path[x][y] != 0 and path[x][y] != -1:
    if path[x][y] == 1:
        path[x][y] = 0
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

            return True

    # if path[x][y] != 0:   # 물에 잠기지 않는 지역 중
    #     path[x][y] = 0  # 방문 처리
        
    #     # print('위치 : ', (x, y))
    #     dfs(x-1, y)
    #     dfs(x+1, y)
    #     dfs(x, y-1)
    #     dfs(x, y+1)
 
    #     return True
    return False

t = 0
while(t <= len(ran)-1):
    cnt = 0
    # path = copy_path
    for i in range(n):
        for j in range(n):
            if path[i][j] <= ran[t]:
                path[i][j] = 0
            else:
                path[i][j] = 1
    # path를 ran[t] 설정에 따라 다시 설정해주어야 함
    # path = copy_path
    print(path)
    # print('dfs 수행')            
    for i in range(n):
        for j in range(n):
            if path[i][j] == 1:
                if dfs(i, j) == True: cnt += 1
                # dfs(i, j)
                # cnt += 1
    print(cnt)
    # if ans < cnt: 
    #     ans = cnt
    ans = max(ans, cnt)
    t += 1
    path = copy_path.copy()
    
print('최대 안전 영역 개수 : ', ans)

