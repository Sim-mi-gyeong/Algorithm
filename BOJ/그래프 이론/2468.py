# 안전 영역
# 높이가 4 이하인 지점 잠기고,
# 물에 잠긴 지역의 제외하고 [상하좌우]로만 이어진 구역 개수
n = int(input())
path = [list(map(int, input().split())) for _ in range(n)]
ans = 0
# 범위 정하기
ran = list()
for i in range(n):
    for j in range(n):
        if path[i][j] not in ran: ran.append(path[i][j])
ran.sort()
print(ran)
cnt = 0
def dfs(x, y):
    global cnt
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
   
    # if path[x][y] == 0:
    #     pass
    # print(path[x][y])
    if path[x][y] != 0:   # 물에 잠기지 않는 지역 중
        path[x][y] = 0  # 방문 처리
        
        # print('위치 : ', (x, y))
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        # path[x][y] = 0  # 방문 처리
        # print('위치 : ', (x, y))
        # dfs(x-1, y)
        # dfs(x+1, y)
        # dfs(x, y-1)
        # dfs(x, y+1)
 
        return True
 
t = 0
while(t <= len(ran)-1):
    cnt = 0
    print(ran[t], '가 제한일 때')
    for i in range(n):
        for j in range(n):
            if path[i][j] <= ran[t]:
                path[i][j] = 0

            # if path[i][j] != 0:
            #     if dfs(i, j): 
            #         cnt += 1
                    # answer.append(cnt)
 
    # print('dfs 수행')            
    for i in range(n):
        for j in range(n):
            if path[i][j] != 0:
                if dfs(i, j): cnt += 1
                # dfs(i, j)
                # cnt += 1
 
    if ans < cnt: ans = cnt
    t += 1
    
print('최대 안전 영역 개수 : ', ans)

