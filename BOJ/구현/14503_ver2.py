# 로봇 청소기

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())
visited = [[False] * m for _ in range(n)]   # 방문하지 않은 상태
lst = [list(map(int, input().split())) for _ in range(n)]
# 북(0) -> 서(3) -> 남(2) -> 동(1) 순서로 돌아야 하며, 
# 회전 방향(d) 를 index로 표현 & 회전 방향으로 이동하는 것을 dx, dy로 표현
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 처음 시작 위치부터
# 현재 위치 방문 처리 -> 2
visited[r][c] = True
cnt = 1
dir = 0   # 회전(탐색) 횟수

while True:
    for i in range(len(dx)):
        # 0 -> 3 -> 2 -> 1 순서로 만들어주기 위한 표현
        nx = r + dx[(d + 3) % 4]
        ny = c + dy[(d + 3) % 4]
        d = (d + 3) % 4    # d = (d-1) % 4
        
        # 청소할 공간이 있는지 확인(2-1)
        if lst[nx][ny] == 0 and visited[nx][ny] == False:
            visited[nx][ny] = True
            r, c = nx, ny
            cnt += 1
            dir = 0    # 회전 횟수 초기화
            break      # 회전 중단 -> 다음으로
        #  다음 for loop 회전(2-2)
        else: dir += 1

     # 4 방향으로 모두 회전한 경우
    if dir == 4:
        # 후진 했을 때의 위치
        nx = r - dx[d]
        ny = c - dy[d]
        # 2-3
        if lst[nx][ny] == 0:  
            r, c = nx, ny
            dir = 0
        else:   # 뒤로 이동하려는 위치가 벽인 경우(2-4)
            print(cnt)
            break

# while True:

#     for _ in range(len(dx)):
#         # 0 -> 3 -> 2 -> 1 순서로 만들어주기 위한 표현
#         nx = r + dx[(d + 3) % 4]
#         ny = c + dy[(d + 3) % 4]
#         # 회전
#         d = (d + 3) % 4   # d = (d-1) % 4

#         # 청소할 공간이 있는지 확인(2-1)
#         if 0 <= nx < n and 0 <= ny < m :
#             if lst[nx][ny] == 0 and visited[nx][ny] == False:
#                 visited[nx][ny] = True
#                 r, c = nx, ny
#                 cnt += 1
#                 dir = 0   # 회전 횟수 초기화
#                 break   # 회전 중단 -> 다음으로
#             #  다음 for loop 회전(2-2)
#             else: dir += 1

#     # 4 방향으로 모두 회전한 경우
#     if dir == 4:
#         # 후진
#         nx = r - dx[d]
#         ny = c - dy[d]   
#         # 뒤로 이동하려는 위치가 벽인 경우(2-4)
#         if 0 <= nx < n and 0 <= ny < m:
#             if lst[nx][ny] == 0:  
#                 r, c = nx, ny
#                 dir = 0
#             else:    # 2-3
#                 print(cnt)
#                 break