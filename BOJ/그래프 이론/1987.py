# 알파벳
# 어느 방향으로, 먼저 나아가는지에 따라 cnt 수가 다름 => 최대 cnt 가 아닌 경우 백트래킹 필요

import sys
sys.setrecursionlimit(10**9)

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[0] * c for _ in range(r)]
dupli = [] 
maxCnt = 0

def dfs(x, y, board, visited, cnt):
    global maxCnt

    # if maxCnt < cnt: maxCnt = cnt   # 다시 돌아오는 경우, 최댓값 저장

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < r and 0 <= ny < c:  
            if board[nx][ny] not in dupli:
                dupli.append(board[nx][ny])
                # cnt += 1   
                # 함수 내부에서 cnt += 1 을 해주면 기본 함수에서의 cnt 값에도 영향을 주기 때문에 함수 호출 시 바로 cnt += 1을 해주어야 함
                dfs(nx, ny, board, visited, cnt + 1)
                dupli.remove(board[nx][ny])   # 백트래킹

    if maxCnt < cnt: maxCnt = cnt   # 함수 호출할 때마다, 최댓값 저장

dupli.append(board[0][0])
dfs(0, 0, board, visited, 1)
print(maxCnt)